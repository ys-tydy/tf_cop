# Terraform automatic reviewer

terraform scripts checker.<br>
This package helps you to review your tf script.<br>
(ex: confirm add logging rule to all s3 bucket)

# TOC
<!-- TOC -->

- [Installation](#Installation)
- [Usage](#Usage)
- [Review_book yaml rule](#Review_book)

<!-- /TOC -->
## Installation

```shell
$ pip install tf_cop
```


## Usage
### 1. cli use
at your console

```shell
$ tfcop TERRAFORM_ROOT_PATH REVIEW_BOOK_ROOT_PATH(optional)
```

sample output

```shell
☁  tf_cop [master] ⚡ tfcop test

==========================================================
RESOURCE AWS_S3_BUCKET.TEST_TF_REVIEW_BUCKET
==========================================================
[WARN] desc_checker : description not use
{   'acl': 'private',
    'bucket': '${terraform.env}-tf-review-bucket'}
[ALERT] tag_checker : tags not use
{   'acl': 'private',
    'bucket': '${terraform.env}-tf-review-bucket'}

==========================================================
RESOURCE AWS_S3_BUCKET.TEST_TF_REVIEW_BUCKET2
==========================================================
[WARN] desc_checker : description not use
{   'acl': 'private',
    'bucket': '${terraform.env}-tf-review-bucket2',
    'lifecycle_rule': {...},
    'logging': {...},
    'tags': {...}}
[PASS] tag_checker : passed
[PASS] name_checker : passed
[PASS] env_checker : passed


 =======================
| RESOURCE NUM  : 2     |
| SKIP NUM      : 0     |
| PASS NUM      : 3     |
| WARN NUM      : 2     |
| ALERT NUM     : 1     |
 =======================
```
### 2. module use
#### do review
pass `terraform root path` & `review_book root path`

```python
import tf_cop

if __name__ == '__main__':
    test = tf_cop.TfCop()
    test.tf_review("./test", "./review_book_default")
```

#### get output

```python
    output = test.output(color_flg=True)
    print(output["output_log"])
    print(output["output_summary_log"])
    print(output["program_error_log"])
    print(output["system_log"])
```

## Review_book yaml rule

|key  |description  |required|
|---|---|---|
|title  |test title|required|
|desc  |description for test|option|
|mode|test mode (existance\|value\|nested)|required|
|key|test target key (ex. tags)|required|
|value|correct value regex|option|
|nest|for nested test|option|
|warn|for warn message|option (default False)|

### existance test
check if target key is exist.<br>
(ex. description)

### value test
check if target value is correct.<br>
(ex. name = "(prd|stg|dev)-s3-.*-terraform")

### nested test
test to nested key_value
```hcl
tags {
    Name = "${terraform.env}-tf-review-bucket"
    Env = "dev"
}
```

## Testing
`python test.py`

## Sample usage
test terraform files using docker.

```
├── Dockerfile
├── main.py
└── requirements.txt
```

```dockerfile
FROM python:3.6

RUN apt-get update
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

WORKDIR /tmp

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python","main.py"]
```


```python
import tf_cop

if __name__ == '__main__':
    test = tf_cop.TfCop()
    test.tf_review("./terraform", "./review_book")

    output = test.output(color_flg=True)
    print(output["output_log"])
    print(output["output_summary_log"])
    print(output["program_error_log"])
```

set `TF_ROOT_PATH` & `REVIEW_BOOK_PATH`

```bash
docker build -t tf_cop .
docker run \
      -v `pwd`/${TF_ROOT_PATH}:/tmp/terraform \
      -v `pwd`/${REVIEW_BOOK_PATH}:/tmp/review_book \
      tf_cop
```

## Author
ys-tydy

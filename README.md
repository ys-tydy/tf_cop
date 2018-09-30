# Terraform automatic reviewer

terraform scripts checker.<br>
This package helps you to review your tf script.<br>
(ex: confirm add logging rule to all s3 bucket)


## Installation

```bash
$ pip install tf_cop
```


## Usage
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

|key  |description  |
|---|---|
|title  |test title|
|desc  |description for test|
|mode|test mode (existance|value|nested)|
|key|test target key (ex. tags)|
|value|correct value regex|
|nest|for nested test|

### existance test
check if target key is exist.<br>
(ex. description)

### value test
check if target value is correct.<br>
(ex. name = "(prd|stg|dev)-s3-.*-terraform")

### nested test
test to nested key_value
```json
tags {
    Name = "${terraform.env}-tf-review-bucket"
    Env = "dev"
    }
```

## Testing
`python test.py`

## Author
ys-tydy

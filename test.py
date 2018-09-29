import tf_cop

if __name__ == '__main__':
    test = tf_cop.TfCop()
    test.tf_review("./test", "./review_book_default")
    with open("./test/ignore_test_output.txt", mode='w') as f:
        f.write(test.result())

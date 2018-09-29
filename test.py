import tf_cop

if __name__ == '__main__':
    test = tf_cop.TfCop()
    test.tf_review("./test", "./review_book_default")
    with open("./test/ignore_test_result.txt", mode='w') as f:
        f.write(test.result())
    with open("./test/ignore_test_result_summary.txt", mode='w') as f:
        f.write(test.result_summary())
    with open("./test/ignore_test_program_error_log.txt", mode='w') as f:
        f.write(test.program_error_log())

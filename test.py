import tf_cop

if __name__ == '__main__':
    test = tf_cop.TfCop()
    test.tf_review("./test", "./review_book")
    with open("./test/ignore_test_result.log", mode='w') as f:
        f.write(test.result())
    with open("./test/ignore_test_result_summary.log", mode='w') as f:
        test_summary = test.result_summary()
        f.write(test_summary)
    with open("./test/ignore_test_program_error_log.log", mode='w') as f:
        test_program_error_log = test.program_error_log()
        f.write(test_program_error_log)
    with open("./test/ignore_test_system_log.log", mode='w') as f:
        test_system_log = test.system_log()
        f.write(test_system_log)
    print(test_summary)
    print(test_program_error_log)
    print(test_system_log)

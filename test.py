import tf_cop

if __name__ == '__main__':
    test = tf_cop.TfCop()
    test.tf_review("./test", "./review_book")
    output = test.output()
    with open("./test/ignore_test_result.log", mode='w') as f:
        f.write(output["output_log"])
    with open("./test/ignore_test_result_summary.log", mode='w') as f:
        f.write(output["output_summary_log"])
    with open("./test/ignore_test_program_error_log.log", mode='w') as f:
        f.write(output["program_error_log"])
    with open("./test/ignore_test_system_log.log", mode='w') as f:
        f.write(output["system_log"])
    print(output["output_summary_log"])
    print(output["program_error_log"])
    print(output["system_log"])

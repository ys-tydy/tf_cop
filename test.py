import tf_cop

if __name__ == '__main__':
    test = tf_cop.TfCop("./test")
    test.tf_review()

    output = test.output(color_flg=True)
    print(output)

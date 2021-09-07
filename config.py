def config():
    filename = "configfile.config"
    contents = open(filename).read()
    config_contents = eval(contents)
    filename = config_contents["filename"]
    input_filename = config_contents["input_filename"]
    log_filename = config_contents["log_filename"]
    classes = config_contents["classes"]
    methods = config_contents["methods"]

    print(filename)
    print(input_filename)
    print(log_filename)
    print(classes)
    print(methods)


config()

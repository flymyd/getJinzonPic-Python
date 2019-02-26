def logger(mkpath,towrite):
    log_file = open(mkpath + "log.txt", 'a')
    log_file.write(towrite)
    log_file.close()


def recorder(mkpath,towrite):
    record_file = open(mkpath + "record.txt", 'a')
    record_file.write(towrite)
    record_file.close()
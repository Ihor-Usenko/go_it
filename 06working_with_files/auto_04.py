employee = "Drake Mikelsson,19"
path = 'text.txt'
fn = open(path, 'a')
position = fn.tell()
fn.write(employee + '\n')
fn.close()
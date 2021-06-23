import os


path = "E:\\projects\\web Crawler"
extend = "\\"

#creating a seperate project for each target
def create_dir(directory):
    
    if not os.path.exists(directory):
        print("[+] Creating new project :"+ directory)
        os.makedirs(directory)
    

# create a queue and crawled files

def create_data_files(project_name, base_url):
    queue =path + extend + project_name+ extend + 'queue.txt'
    crawled = path + extend + project_name + extend +'crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, '')

#writing data on queue and crawl files

def write_file(file_path, data):
    f = open(file_path, 'w')
    f.write(data)
    f.close()

#addding other data onto an existing file

def append_to_file(file_path, data):
    with open(file_path, 'a') as f:
        f.write(data + '\n')

#delete the content from the file

def delete_file_data(file_path):
    with open(file_path, 'w'):
        pass

#read a file and convert each line to set items

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    
    return results

# converting set to file

def set_to_file(links, file):
    delete_file_data(file)
    for link in sorted(links):
        append_to_file(file, link)
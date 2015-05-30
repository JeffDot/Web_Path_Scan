import argparse
import requests
import thread
import urllib
def scan_path() :
    return
class web_path_scan_class :
    def __init__(self) :
        print "-----------------------"
        para = argparse.ArgumentParser(description = "get para")
        para.add_argument('-u' ,'--url' ,help = "the url of the website you want to scan")
        para.add_argument('-t' ,'--threads' ,type = int ,default = 10 ,help = "set threads")
        args = para.parse_args()
        self.url = args.url
        self.threads = args.threads
        print self.url
        self.dict_list = []
        with open('backdoor.txt' ,'rb') as dictionary :
            for line in dictionary.readlines() :
                line = line.strip('\n')
                self.dict_list.append(line)
        
        self.step_size = len(self.dict_list)/self.threads
        self.success_list = []
        self.doubtable_list = []
        self.failure_list = []
        return
    def scan(self) :
        req = requests.get(self.url)
        success_status_code = req.status_code
        req = requests.get(self.url + '/i_wont_be_the_right_path.php')
        fail_status_code = req.status_code
        """dict_curr = self.dict_list[order*self.step_size:(order+1)*self.step_size]"""
        for item in self.dict_list :            
            tmp = self.url + '/' + item
            print "     trying .... %s " % item
            try :
                req = requests.get(tmp)
            except Exception ,msg :
                print "trying:" ,tmp ,'happen:' ,msg         
            if req.status_code == success_status_code :
                print '[success]%s : %d' % (tmp ,req.status_code)
                self.success_list.append(tmp)
            elif req.status_code == fail_status_code :
                self.failure_list.append(tmp)
            else :
                self.doubtable_list.append(tmp)
            
        return
    def return_success(self) :
        print self.success_list


                

if __name__ == '__main__' :
    a = web_path_scan_class()
    a.scan()
    
    print a.return_success()


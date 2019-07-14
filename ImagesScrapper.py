from selenium import webdriver
import time
import re,os
import urllib.parse
import urllib.request as grab
from pattern.web import DOM,URL
class GoogleImageExtractor(object):
    def __init__(self,search_Key="Note for Class",add_counter=0):
        if type(search_Key)==str:
            self.search_key_list = search_Key
        else:
            print("Values came are not in the order they expected")

        self.total_images_needed=1000
        self.prefix_of_search="https://www.google.com.sg/search?q="
        self.postfix_of_search="&source=lnms&tbm=isch"
        self.pic_url_list=[]
        self.pic_counter=1+add_counter
        self.page_source=""
        self.target_url=""

    def reformat_search(self):
        query=self.search_key_list
        query=query.split()
        query='+'.join(query)
        self.search_key_list=query

    def formed_search_url(self):
        self.reformat_search()
        self.target_url=self.prefix_of_search+self.search_key_list+self.postfix_of_search

    def retrieve_source_for_html(self):
        driver=webdriver.ChromeOptions()
        browser = webdriver.Chrome("C:\\Users\\I514338\Desktop\\Image Scrapper\\WebDriver\\chromedriver.exe",options=driver)
        browser.get(self.target_url)
        try:
            for _ in range(15):
                browser.execute_script("window.scrollTo(0,30000)")
                time.sleep(2)
                # element=browser.find_element_by_id("smb")
                # print(element,'hey')
                # if(element):
                #     element.click()
        except:
            print("not able to find")
            browser.quit()
        self.page_source=browser.page_source
        browser.close()

    def url_from_source(self):
        dom=DOM(self.page_source)
        tag_list=dom('a.rg_l')
        # print(self.pic_counter)
        for tag in tag_list:
            if self.pic_counter>2000:
                break
            else:
                tar_str=re.search('imgurl=(.*)&imgrefurl',tag.attributes['href'])
                try:
                    # print(tar_str)
                    self.pic_url_list.append(tar_str.group(1))
                except:
                    print("Error parsing")


    def downloading_all_photos(self):
        self.formed_search_url()
        self.retrieve_source_for_html()
        self.url_from_source()
        for url_link in self.pic_url_list:
            pic_prefix_str='Notes'+str(self.pic_counter)
            self.download_single_image(urllib.parse.unquote(url_link),pic_prefix_str)

    def download_single_image(self,url_link,pic_prefix_str):
        # print(url_link,self.pic_counter)
        file_ext=os.path.splitext(url_link)[1]
        temp_filename=pic_prefix_str+file_ext
        temp_file_fullname=os.path.join('C:\\Users\\I514338\\Desktop\\Image Scrapper\\Images',temp_filename)
        valid_img_ext_list=['.png','.jpg','jpeg','.gif']
        url=URL(url_link)
        if file_ext not in valid_img_ext_list:
            return
        f=open(temp_file_fullname,'wb')
        try:
            # print(url_link,temp_file_fullname)
            grab.urlretrieve(url_link,temp_file_fullname)
            self.pic_counter+=1
        except:
            print('Problem with downloading image')
        f.close()


if __name__=='__main__':
    fetcherobj=GoogleImageExtractor()
    fetcherobj.downloading_all_photos()
    fetcherobj2=GoogleImageExtractor("Some random pics",1000)
    fetcherobj2.downloading_all_photos()


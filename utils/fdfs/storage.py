from django.core.files.storage import Storage
from django.core import settings
from py3Fdfs.client import fdfs_client

class FDFSStorage(Storage):
    # fastDFS存储类
    def __init__(self, client_conf=None, base_url=None):
        '''傳參初始化'''
        if client_conf is None:
            client_conf=settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url

    def open(self, name, mode='rb'):
        # 打开文件时使用。
        pass

    def save(self, name, content):
        # 保存文件时使用。
        # name 您选者的上传文件的名字
        # content 包含您上传内容的content对象.

        # 创建一个fdfs_clients
        client = fdfs_client(self.client_conf)

        # 上传文件 fast dfs中
        res = client.uploal_by_buffer(content.read())

       #  dict
    #         {
    #          'Group name':group_name,
    #          'Remote file_id':remote_file_id,
    #             'Status':'Upload successed',
    #             'Local file name':'',
    #             'Uploaded size':'upload_size',
    #             'Storage IP': storage_ip
    #         }
        if res.get('Status') != 'Upload successed':
            # 上傳失敗
            raise Exception('上傳文件到fast dfs失敗.')
        # 獲取返回的Id
        filename = res.get('Remote file_id')

        return filename

    def exists(self, name):
        # django判斷文件名是否可用
        return False
    def url(self, name):
        # django返回訪問url路徑
        return self.base_url+name

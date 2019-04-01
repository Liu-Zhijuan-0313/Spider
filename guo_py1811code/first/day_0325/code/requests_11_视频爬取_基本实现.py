import requests


def download_file(url, path):
    # stream=True流的方式下载
    with requests.get(url, stream=True) as r:
        chunk_size = 1024
        # content-length读取视频的大小
        content_size = int(r.headers['content-length'])
        print('下载开始。。。')
        with open(path, "wb") as f:
            # 相应对象迭代的方法
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    print('下载结束。。。')


if __name__ == '__main__':
    url = 'https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo-transcode/51722773_98a3bb47a51fef46145630154f007ddc_0.mp4'
    path = './videos/v.mp4'
    download_file(url, path)


from requests.api import request


'''
不好判断传入的method。舍弃
'''
def method(func):
    '''
    解释器,
    1.先进行func(get,post。。。)请求
    2.然后返回结果,或者logger记录
    3.在运行get内的方法
    '''
    def send(self,*args,**kwargs):
        results = func(self,*args,**kwargs)
        return results
    return send

class Myrequest:
    @method
    def get(url, params=None, **kwargs):
        return request("get", url, params=params, **kwargs)

    @method
    def options(url, **kwargs):
        return request("options", url, **kwargs)

    @method
    def head(url, **kwargs):
        kwargs.setdefault("allow_redirects", False)
        return request("head", url, **kwargs)

    @method
    def post(url, data=None, json=None, **kwargs):
        return request("post", url, data=data, json=json, **kwargs)

    @method
    def put(url, data=None, **kwargs):
        return request("put", url, data=data, **kwargs)

    @method
    def patch(url, data=None, **kwargs):
        return request("patch", url, data=data, **kwargs)

    @method
    def delete(url, **kwargs):
        return request("delete", url, **kwargs)


if __name__ == '__main__':
    url = 'http://127.0.0.1:1999/update'
    payload = {
        "username":"name",
        "password":"12345"
    }
    res = Myrequest.post(url,json=payload)
    print(res.text)
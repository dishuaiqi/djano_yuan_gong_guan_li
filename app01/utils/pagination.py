'''
自定义的分页组件

'''
from django.utils.safestring import mark_safe
class Pagination(object):

    def __init__(self,request,mobile_list, page_gram="page",page_num = 15,plus=1):

        '''
        :param request: 请求的对象
        :param mobile_list: 符合条件的数据（根据这个数据进行分页处理）
        :param page_gram:每页显示多少数据
        :param page_num:在URL中传递的获取分页的参数，例如/mobile/list/?page=6
        :param plus:显示当前页的前几页或后几页

        若想使用页码，需要在页面后加上如下代码
      <ul class="pagination">

        {{ page_str }}

      </ul>


        '''

        # page = int(request.GET.get(page_gram, 1))  #此传值如果传过来的是字母或者负值就会出现问题

        import copy
        query_dict = copy.deepcopy(request.GET)

        query_dict._mutable = True  # 把这个数据修改之后，就能改动url中的值

        self.query_dict=query_dict
        # query_dict.setlist('page', [11])
        # print(query_dict.urlencode())

        self.page_gram=page_gram
        page = request.GET.get(page_gram, '1')
        if page.isdecimal():  #判断page是否为一个十进制的数
            page=int(page)
        else:
            page=1
        self.page=page   #把page封装进去object中
        # print(page)
        # page_num = 15  #指每页显示多少数据
        self.page_num=page_num

        self.start_page = page_num * page - page_num
        self.end_page = page_num * page          #把分页的起始值和终止值都封装进去
        # print(self.end_page)
        self.page_mobile_list=mobile_list[self.start_page:self.end_page]   #分页切片
        print(self.page_mobile_list)
        total_count = mobile_list.count()  # 求总共有多少条数据
        # print(total_count)
        total_page, yu = divmod(total_count, page_num)  # 得到整数和余数
        # print(total_page)
        # print(yu)
        if yu > 0:
            total_page = total_page + 1
            # print(total_page)
        self.total_page=total_page
        self.plus=plus
    def html(self):
        if self.total_page <= 2*self.plus+1:  # 此判断主要用来表示当前后页小于11时，不出现负数，以及不展示没有数据的页面
            star_p = 1
            end_p = self.total_page
        else:
            if self.page<=self.plus:
                star_p=1
                end_p=2*self.plus+1
            else:
            # 当前页>5    当前页+5>总页码
                if (self.page + self.plus) > self.total_page:
                    star_p = self.total_page - 2 * self.plus
                    end_p = self.total_page
                else:
                    star_p = self.page - self.plus
                    end_p = self.page + self.plus
        print(end_p)
        page_list_num = []
        # 添加首页
        self.query_dict.setlist(self.page_gram, [1])

        # print(self.query_dict.urlencode())
        sy = '<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode())
        page_list_num.append(sy)

        # 添加上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_gram, [self.page-1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_gram, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())

        page_list_num.append(prev)
        for i in range(star_p, end_p + 1):
            self.query_dict.setlist(self.page_gram, [i])
            if i == self.page:  # 用来展示当前页
                els = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                els = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_list_num.append(els)

        # 添加下一页
        if self.page < self.total_page:
            self.query_dict.setlist(self.page_gram, [self.page+1])
            prev_h = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_gram, [self.total_page])
            prev_h = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_list_num.append(prev_h)
        # 添加尾页
        self.query_dict.setlist(self.page_gram, [self.total_page])
        wy = '<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode())
        page_list_num.append(wy)

        # 添加 输入页码跳转
        search_string = '''
             <li>
                <form style="float: left;margin-left: -1px" method="get">
                    <input name="page"
                           style="position: relative;float: left;display: inline-block;width: 88px;border-radius: 0;"
                           type="text" class="form-control" placeholder="页码">
                    <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
                </form>
            </li>
        '''
        page_list_num.append(search_string)
        page_str = ''.join(page_list_num)

          # 需要导入这个库，标记说明此字符串是安全的，这样传入后台就可以使用了

        page_str = mark_safe(page_str)
        return page_str
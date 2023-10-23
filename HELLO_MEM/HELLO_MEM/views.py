from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import pymysql
from HELLO_MEM.dao_mem import DaoMem
 
def mem_list(request):
    de = DaoMem()
    mems = de.selectList()
    return render(request, "mem_list.html",{'mems':mems})

def mem_detail(request):
    m_id = request.GET.get('m_id','')
    de = DaoMem()
    mem = de.selectOne(m_id)
    print("mem", mem)
    return render(request, "mem_detail.html",{'mem':mem})

def mem_mod(request):
    m_id = request.GET.get('m_id','')
    de = DaoMem()
    mem = de.selectOne(m_id)
    print("mem", mem)
    return render(request, "mem_mod.html",{'mem':mem})

def mem_mod_act(request):
    m_id = request.POST['m_id']
    m_nm = request.POST['m_nm']
    tel = request.POST['tel']
    addr = request.POST['addr']
    de = DaoMem()
    cnt = de.update(m_id, m_nm, tel, addr)
    
    return render(request, "mem_mod_act.html",{'cnt':cnt})

def mem_add(request):
    return render(request, "mem_add.html")

def mem_add_act(request):
    m_id = request.POST['m_id']
    m_nm = request.POST['m_nm']
    tel = request.POST['tel']
    addr = request.POST['addr']
    de = DaoMem()
    cnt = de.insert(m_id, m_nm, tel, addr)
    
    return render(request, "mem_add_act.html",{'cnt':cnt})

def mem_del_act(request):
    m_id = request.POST['m_id']
    de = DaoMem()
    cnt = de.delete(m_id)
    
    return render(request, "mem_del_act.html",{'cnt':cnt})
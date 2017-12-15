#coding:utf-8
import win32com.client
count=1
wmi=win32com.client.GetObject('winmgmts:')
for p in wmi.InstancesOf('win32_process'):
    print p.Name, p.Properties_('ProcessId'), \
        int(p.Properties_('UserModeTime').Value)+int(p.Properties_('KernelModeTime').Value)
    children=wmi.ExecQuery('Select * from win32_process where ParentProcessId=%s' %p.Properties_('ProcessId'))
    for child in children:

        print '\t','第%s进程为：'%count,child.Name,child.Properties_('ProcessId'), \
            int(child.Properties_('UserModeTime').Value)+int(child.Properties_('KernelModeTime').Value)
        count+=1
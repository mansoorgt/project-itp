
from django.urls import path 
from .import views 

urlpatterns = [
    

        #build pass
        path('build_pass_submit',views.registration.build_pass_submit,name='build_pass_submit'),
        #event pass
        path('event_pass_submit',views.registration.event_pass_submit,name='event_pass_submit'),
        #vapp pass
        path('vapp_pass_submit',views.registration.vapp_pass_submit,name='vapp_pass_submit'),
        
        path('registration_success',views.registration.registration_success,name='registration_success'),
        
        #check existence 
        path('check_user_existece',views.registration.user_check_existence,name='check_user_existece'),
        
        path('test',views.registration.test_email,name='test'),
        
        #bulk reg
        path('build_bulk_submit',views.registration.submit_bulk_build_pass,name='build_bulk_submit'),
        path('vapp_bulk_submit',views.registration.submit_bulk_vapp_pass,name='vapp_bulk_submit'),
    #login 
    path('',views.Login.login_page,name='login'),
     path('logout',views.Login.log_out,name='logout'),
        #login validiate
        path('validitate',views.Login.validitate_login,name='validiate'),
    #dashboard
    path('dashboard',views.Dashboard.dashboard_page,name='dashboard'),
    
    #Table_page
    path('tables',views.Tablepage.table_page,name='tables'),
    path('update_status',views.Tablepage.update_status,name='update_status'),
    path('update_print_status',views.Tablepage.update_print_status,name='update_print_status'),
    path('change_category_vapp',views.Tablepage.change_category_vapp,name='change_category_vapp'),
    path('del_reg',views.Tablepage.del_registration,name='del_reg'),
    path('edit_submit_buildtable',views.Tablepage.edit_submit_build_pass,name='edit_submit_buildtable'),
    path('edit_submit_eventtable',views.Tablepage.edit_submit_event_pass,name='edit_submit_eventtable'),
    path('edit_submit_vapptable',views.Tablepage.edit_submit_vapp_pass,name='edit_submit_vapptable'),
    path('upate_bulk_status',views.Tablepage.update_bulk_status,name='upate_bulk_status'),
    path('get_profile_details',views.Tablepage.get_profile_details,name='get_profile_details'),
    path('change_remark',views.Tablepage.change_remark,name='change_remark'),
    path('bulk_edit',views.Tablepage.edit_bulk,name='bulk_edit'),
    #send email 
        path('send_rejection_mail',views.Tablepage.send_reason_mail,name='send_rejection_mail'),
        path('send_approved_mail',views.Tablepage.send_approved_mail,name='send_approved_mail'),
    #print
    path('print_vapp_vip/<int:id>',views.Tablepage.print_vapp_vip_id,name='print_vapp_vip'),
    path('print_build_pass/<int:id>',views.Tablepage.print_build_id,name='print_build_pass'),
    path('print_event_pass/<int:id>',views.Tablepage.print_event_id,name='print_event_pass'),
    path('data_bulk',views.Tablepage.get_data_bulk,name='data_bulk'),
    path('print_vapp_bulk',views.Tablepage.print_vapp_bulk,name='print_vapp_bulk'),
    path('print_build_bulk',views.Tablepage.print_build_bulk,name='print_build_bulk'),
    path('print_event_bulk',views.Tablepage.print_event_bulk,name='print_event_bulk'),
    #download images
    path('get_image_urls',views.Tablepage.get_img_urls,name='get_image_urls'),
    
    
    #update front page
    path('update_front_page',views.Tablepage.update_front_page_in_ajax,name='update_front_page'),
    path('update_bulk_print_page',views.Tablepage.update_bulk_print_page,name='update_bulk_print_page'),
    
    path('get_new_data',views.Tablepage.get_new_data,name='get_new_data'),
    path('build_pass_page',views.Tablepage.build_table_page,name='build_pass_page'),
    path('event_pass_page',views.Tablepage.event_table_page,name='event_pass_page'),
    path('vapp_pass_page',views.Tablepage.vapp_table_page,name='vapp_pass_page'),
    
    #report 
    
    path('report',views.Report.report_page,name='report'),
    path('reportGetData',views.Report.getReportData,name='reportGetData')
]

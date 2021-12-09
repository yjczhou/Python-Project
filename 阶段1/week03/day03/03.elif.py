# coding:utf-8

# elif 对于命题的非第一次的多种判断，每一种判断条件对应一组业务代码
# 对于首次if判断不满足后，其他条件的判断语句

# if bool_result:
#   do
# elif bool_result:
#   elifdo
# elif bool_result:
#   dlifdo
# else
#   do

dewei_status ='sleep'
if dewei_status == 'hunger':
    print('xiaomu invites dewei to dinner')
elif dewei_status == 'thirsty':
    print('xiaomu give dewei some drick')
elif dewei_status == 'sleepy':
    print('dewi want to sleep')
else:
    print('dewei statud is good')

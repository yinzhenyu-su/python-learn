def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
profile=build_profile('尹','振宇',评分='100',等级='100',技能='未知',潜力='未知')
print(profile)
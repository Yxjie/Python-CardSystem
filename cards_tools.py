# 记录所有的名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    # 1.提示用户输入内容
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")
    # 2.使用输入内容创建名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3.将名片字典追加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示用户添加成功
    print("添加 %s 名片成功" % name_str)


def show_all():
    """显示全部"""
    print("-" * 50)
    print("显示所有名片")

    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片!!!")
        return

        # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    # 换行作用
    print("")
    # 打印分割线
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))


def search_card():
    """查询名片"""
    print("-" * 50)
    print("查询名片")

    find_name = input("请输入要搜索的姓名：")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            # 打印分割线
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
            # 针对找到名片 执行修改删除操作
            deal_dict(card_dict)
            break
    else:
        print("抱歉没有找到 %s" % find_name)


def deal_dict(find_dict):
    action_str = input("请选择需要执行的操作：[1]修改 [2]删除 [0]返回上级菜单：")
    if action_str == "1":
        find_dict["name"] = input_user_info(find_dict["name"], "请输入姓名【回车不修改】：")
        find_dict["phone"] = input_user_info(find_dict["phone"], "请输入电话【回车不修改】：")
        find_dict["qq"] = input_user_info(find_dict["qq"], "请输入QQ【回车不修改】:")
        find_dict["email"] = input_user_info(find_dict["email"], "请输入邮箱【回车不修改】：")

    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功")


def input_user_info(dict_value, tip_message):
    """自定义输入框
    :param dict_value: 
    :param tip_message: 
    :return: 
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value

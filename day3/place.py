place = {
    '山东': {
        '青岛': ['四方', '黄岛', '崂山', '李沧', '城阳'],
        '济南': ['历城', '槐荫', '高新', '长青', '章丘'],
        '烟台': ['龙口', '莱山', '牟平', '蓬莱', '招远']
    },
    '江苏': {
        '苏州': ['沧浪', '相城', '平江', '吴中', '昆山'],
        '南京': ['白下', '秦淮', '浦口', '栖霞', '江宁'],
        '无锡': ['崇安', '南长', '北塘', '锡山', '江阴']
    },
    '浙江': {
        '杭州': ['西湖', '江干', '下城', '上城', '滨江'],
        '宁波': ['海曙', '江东', '江北', '镇海', '余姚'],
        '温州': ['鹿城', '龙湾', '乐清', '瑞安', '永嘉']
    },
    '安徽': {
        '合肥': ['蜀山', '庐阳', '包河', '经开', '新站'],
        '芜湖': ['镜湖', '鸠江', '无为', '三山', '南陵'],
        '蚌埠': ['蚌山', '龙子湖', '淮上', '怀远', '固镇']
    },
    '广东': {
        '深圳': ['罗湖', '福田', '南山', '宝安', '布吉'],
        '广州': ['天河', '珠海', '越秀', '白云', '黄埔'],
        '东莞': ['莞城', '长安', '虎门', '万江', '大朗']
    }
}


def show():
    while True:
        # 输入省编号
        province_list = list(place.keys())
        show_province(province_list)
        province_choice = input("请输入省编号：")

        if province_choice.isdigit() and 0 < int(province_choice) <= len(province_list):
            while True:
                # 输入市编号
                city_list = list(place[province_list[int(province_choice)-1]].keys())
                show_city(city_list)
                city_choice = input("请输入市编号：")
                if city_choice.isdigit() and 0 < int(city_choice) <= len(city_list):
                    while True:
                        # 进入最底层，只能b（返回）或者q（退出）
                        county_list = place[province_list[int(province_choice)-1]][city_list[int(city_choice)-1]]
                        show_county(county_list)
                        choice = input("请输入b/q：")
                        if choice == "b":
                            break
                        elif choice == "q":
                            return
                        else:
                            print("wrong choice")
                elif city_choice == "q":
                    return
                elif city_choice == "b":
                    break
                else:
                    print("wrong choice")
        elif province_choice == "q":
            return
        else:
            print("wrong choice")


def show_province(province_list):
    print("*********************** 省 ************************")
    for index, province in enumerate(province_list):
        print(index+1, province)


def show_city(city_list):
    print("*********************** 市 ************************")
    for index, city in enumerate(city_list):
        print(index+1, city)


def show_county(county_list):
    print("*********************** 县 ************************")
    for index, county in enumerate(county_list):
        print(index+1, county)


if __name__ == "__main__":
    show()

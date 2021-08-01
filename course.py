# 用來讀course名稱 ，存入txt檔中，之後存成json檔即可
import json

def hasExist( item, list_of_course ) :
    i = 0 
    while ( i < len(list_of_course) ) :
        if ( item == list_of_course[i] ) :
            return True
            
        i = i + 1
    
    return False 

if __name__ == '__main__':
    filename = "course_name.txt"
    f = open(filename,'r', encoding='utf-8')

    # 以下為讀檔
    courses = f.read() # 把全部課程讀進courses中
    list_of_course = []
    item = ""
    i = 0
    while ( i < len(courses) ) : # 將課程一筆一筆存入list中，跳出while之後要寫檔
        if ( courses[i] != "\n" ) : # 完整的item就是課程名稱 如: "認識星空"
            item = item + courses[i] 
        elif( item != "" ) : # 若課程不是空的(該行除了課程名外還有換行)
            if( hasExist( item, list_of_course ) == False ) : # 沒有出現過的課程才加入list中，這樣才不會重複寫入
                list_of_course.append(item)
            item = ""
        i = i + 1
    f.close()
    # 以下為寫檔 寫成txt， 之後存成json檔即可
    is_first_item = True
    f_output = open('course_output.txt', 'w')
    f_output.write("[\n" )
    for item in list_of_course :
        if ( is_first_item == False ) : 
            f_output.write(",\n")
        is_first_item = False
        f_output.write("    {\n" )
        f_output.write( "      \"value\": \"")
        f_output.write(item)
        f_output.write("\",\n")
        f_output.write("      \"synonyms\": [\n        \"")
        f_output.write(item)
        f_output.write("\"\n      ]\n")
        f_output.write("    }" )

    f_output.write("\n  ]" )
    f_output.close()
    
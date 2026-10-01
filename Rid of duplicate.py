student_data={
    "id1":{"name":"John", "classs":"V","subject_integration":"english,maths,science"},
    "id2":{"name":"Sara", "classs":"V","subject_integration":"english,maths,science"},
    "id3":{"name":"John", "classs":"V","subject_integration":"english,maths,science"}
}

result={}
seen_keys=[]


for student_id,details in student_data.items():
    unique_key=(details["name"],details["classs"],details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details




for k,v in result.items():
    print(k,":",v)


grade_book={"Alice": 90, "John": 92,"Bob":85,"Charlie":99,"Diana":95}



total_score=0
for score in grade_book.values():
    total_score+=score
average=total_score/len(grade_book)
print(average)


top_student=max(grade_book,key=grade_book.get)
print("Top student:",top_student,"with score",grade_book[top_student])


bottom_student=min(grade_book,key=grade_book.get)
print("Bottom student:",bottom_student,"with score",grade_book[bottom_student])

name=input("Enter a student's name:")
if name in grade_book:
    print(name,"scored",grade_book[name])
else:
    print("Student not found.")
    
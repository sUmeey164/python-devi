#Bu alıştırmada bir üniversite dersine ait not istatistiklerini yazdıran bir program yazacaksınız.
#Program kullanıcıdan dersteki farklı öğrencilerin sonuçlarını ister.
#  Bunlara sınav puanları ve tamamlanan egzersiz sayıları da dahildir. Program daha sonra sonuçlara göre istatistikleri yazdırır.
#Sınav puanları 0 ile 20 arasında tam sayılardır. Tamamlanan alıştırma sayısı 0 ile 100 arasında tam sayılardır.
#Kullanıcı boş bir satır yazana kadar program kullanıcıdan girdi istemeye devam eder.
#  Tüm satırların geçerli girdi içerdiğini, yani her satırda iki tam sayı olduğunu veya satırın boş olduğunu varsayabilirsiniz.
exam_points = []
exercises_completed = []

while True:
    
    user_input = input("Exam points and exercises completed: ")
    
  
    if not user_input:
        break
    
   
    exam, exercises = map(int, user_input.split())
    
    
    exam_points.append(exam)
    exercises_completed.append(exercises)


total_students = len(exam_points)
if total_students > 0:
    
    total_points = [exam + min(exercise // 10, 10) for exam, exercise in zip(exam_points, exercises_completed)]
    avg_points = sum(total_points) / total_students
    
    
    pass_students = len([grade for grade in total_points if grade >= 8])
    pass_percentage = (pass_students / total_students) * 100
    
   
    grade_distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
    for points in total_points:
        if points >= 18:
            grade_distribution[5] += 1
        elif points >= 15:
            grade_distribution[4] += 1
        elif points >= 12:
            grade_distribution[3] += 1
        elif points >= 8:
            grade_distribution[2] += 1
        elif points >= 5:
            grade_distribution[1] += 1
        else:
            grade_distribution[0] += 1
    
    
    print("\nStatistics:")
    print(f"Points average: {avg_points:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    
    for grade in [5, 4, 3, 2, 1, 0]:
        print(f"  {grade}: {'*' * grade_distribution[grade]}")
else:
    print("No data entered.")
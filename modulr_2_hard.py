print ("Введите выпавшее число")
number=int(input())
Spisok_dlya_perebora=[]
result=[]
# Заполню список для перебора
for i in range(number-1):
  Spisok_dlya_perebora.append(i+1)
# Заполню список результами преобразований 
for i in range(len(Spisok_dlya_perebora)):
  Spisok_vnutrenniy = Spisok_dlya_perebora.copy()
  a=Spisok_vnutrenniy.pop(i)
  for k in range(len(Spisok_vnutrenniy)):
    b=Spisok_vnutrenniy[k]    
    if number%(a+b)==0: #Проверка на дублирование результатов
      c=(a in result) and (b in result)      
      if c==False:
        result.append(a)
        result.append(b)
# Приведу результат к виду, который указан в задании
result_str=""
#print("result=",result)
for i in range(len(result)):
  result_str=result_str+str(result[i])
print (result_str)
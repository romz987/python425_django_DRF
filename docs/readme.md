## Serializers   
В DRF Serializer — это не просто структура, а двусторонний адаптер между JSON и моделью + логика валидации и сохранения.  

После поступления запроса на enpoint, в зависимости от типа запроса, представление вызывает один из классов сериализаторов. Например:  
  
GET /users/     -> UserSerializer     
POST /users/    -> UserCreateSerialzer   
PATCH /users/   -> UserUpdateSerializer  
POST /token/    -> UserTokenObtainPairSerializer   

Далее, сериализатор проверяет входные данные
Вызывает .is_valid() — валидирует поля, запускает кастомные валидаторы (например, PasswordValidator)
Если всё ок — данные попадают в validated_data


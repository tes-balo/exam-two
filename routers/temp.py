# from pydantic import TypeAdapter, BaseModel

class  Test():
	def __init__(self, name: str, age: int) -> None:
		self.name = name
		self.age = age

temp = Test(
	name="Tee",
	age=24
)
data = [{

}]

d1 = {
	"d": {"name": "Tes", "age": 24,},
}

print(repr(temp))
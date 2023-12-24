from models.drinks import DrinkModel
from models.staff_member import StaffMemberModel
from settings import Engine


async def seed_data() -> None:
    staff_members = [
        {
            "name": "K Srinivas Rao",
            "image": "https://upload.wikimedia.org/wikipedia/"
            "en/thumb/5/56/Batman_Logo.svg/1200px-Batman_Logo.svg.png",
            "email": "ksrinivasrao531@gmail.com",
            "mobile": "7789831679",
        },
        {
            "name": "Priyosmita Nandy",
            "image": "https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/"
            "Wonder_Woman_DC_Comics.png/220px-Wonder_Woman_DC_Comics.png",
            "email": "priyosh08@gmail.com",
            "mobile": "8697892238",
        },
    ]

    drinks = [
        {
            "name": "Coffee",
            "image": "https://t4.ftcdn.net/jpg/01/16/61/93/"
            "360_F_116619399_YA611bKNOW35ffK0OiyuaOcjAgXgKBui.jpg",
        },
        {
            "name": "Tea",
            "image": "https://cdn2.foodviva.com/static-content/food-images/"
            "tea-recipes/milk-tea-recipe/milk-tea-recipe.jpg",
        },
        {
            "name": "Water",
            "image": "https://www.sciencenewsforstudents.org/wp-content"
            "/uploads/2020/03/1030_LL_water-1028x579.jpg",
        },
    ]

    staff_member_instances = []
    for staff_member in staff_members:
        staff_member_instance = StaffMemberModel(**staff_member)
        saved_staff_member = await Engine.save(instance=staff_member_instance)
        staff_member_instances.append(saved_staff_member)

    for i, drink in enumerate(drinks):
        staff_member_id = staff_member_instances[i % len(staff_members)]
        drink_instance = DrinkModel(staff_member_id=staff_member_id, **drink)
        await Engine.save(instance=drink_instance)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main=seed_data())

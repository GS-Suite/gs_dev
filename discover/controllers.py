from discover import models as discover_models


async def search(query, filter):

    query = query.split(" ")

    ### process query
    results = set()

    for q in query:
        if filter == "name":
            x = await discover_models.search_user_name(q)
            results = results.union(x)
        elif filter == "username":
            x = await discover_models.search_username(q)
            results = results.union(x)
        elif filter == "email":
            x = await discover_models.search_email(q)
            results = results.union(x)
        else:
            x = await discover_models.search_user_name(q)
            results = results.union(x)

            x = await discover_models.search_username(q)
            results = results.union(x)
    
    #print(results)

    ### search
    return [{
        "username": result.username,
        "first_name": result.first_name,
        "last_name": result.last_name,
        "email": result.email
    } for result in results] 
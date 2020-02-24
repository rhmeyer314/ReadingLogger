function bookSearch() {
        var search = document.getElementById('search').value
        var checkbox;
        document.getElementById('results').innerHTML = ""
        console.log(search)

        $.ajax({
            url: "https://www.googleapis.com/books/v1/volumes?q=" + search + "&maxResults=40",
            dataType: "json",
            success: function (data) {
                console.log(data)
                for (i = 0; i < data.items.length; i++) {
                    results.innerHTML += "<input type='checkbox' name='bookid' value='" + data.items[i].id + "'>" + "<img src='" + data.items[i].volumeInfo.imageLinks.smallThumbnail + "'>"
                        + " " + data.items[i].volumeInfo.title + "<p>"
                }
            },

            type: "GET"
        });


    }


    document.getElementById('button').addEventListener('click', bookSearch, false)
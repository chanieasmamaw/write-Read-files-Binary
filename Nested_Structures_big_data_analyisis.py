DATA = {
  "latest_from_star_wars": [
    {
      "position_on_page": 5,
      "title": "Virtual Premiere | The Mandalorian | Disney+",
      "link": "https://www.youtube.com/watch?v=1qq4Q5n3-nU",
      "channel": {
        "name": "Star Wars",
        "link": "https://www.youtube.com/user/starwars",
        "verified": "true",
        "thumbnail": "https://yt3.ggpht.com/a-/AOh14GgskYzAhYn9cvahFlka1ODJVVGGvbJA4AGorw=s68-c-k-c0x00ffffff-no-rj-mo"
      },
      "published_date": "9 hours ago",
      "views": 57855,
      "length": "29:56",
      "description": "The Mandalorian and the Child continue their journey, facing enemies and rallying allies as they make their way through a ...",
      "extensions": [
        "New"
      ],
      "thumbnail": {
        "static": "https://i.ytimg.com/vi/1qq4Q5n3-nU/hqdefault.jpg?sqp=-oaymwEZCOADEI4CSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCwGKt1H-KNnzAuF_u2C5mfiNGmbg",
        "rich": "https://i.ytimg.com/an_webp/1qq4Q5n3-nU/mqdefault_6s.webp?du=3000&sqp=CIWD9fwF&rs=AOn4CLD82MG25RdVFBTESXsHxrC8jSVYvg"
      }
    },
    {
      "position_on_page": 6,
      "title": "The Mandalorian Virtual Red Carpet Premiere, What Scares the Jedi, and More!",
      "link": "https://www.youtube.com/watch?v=dTR7q_0_YOQ",
      "channel": {
        "name": "Star Wars",
        "link": "https://www.youtube.com/user/starwars",
        "verified": "true",
        "thumbnail": "https://yt3.ggpht.com/a-/AOh14GgskYzAhYn9cvahFlka1ODJVVGGvbJA4AGorw=s68-c-k-c0x00ffffff-no-rj-mo"
      },
      "published_date": "1 day ago",
      "views": 30410,
      "length": "3:30",
      "description": "This week, in Star Wars we announce The Mandalorian Season Two virtual red carpet premiere event, find out what scares the ...",
      "extensions": [
        "New",
        "CC"
      ],
      "thumbnail": {
        "static": "https://i.ytimg.com/vi/dTR7q_0_YOQ/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCq4INL160YpyYcyCmPUgXFMAPVhQ",
        "rich": "https://i.ytimg.com/an_webp/dTR7q_0_YOQ/mqdefault_6s.webp?du=3000&sqp=CLCl9fwF&rs=AOn4CLD0LznG9CI33NgPdTE_HXahIu4dJw"
      }
    },
    {
      "position_on_page": "hidden",
      "title": "The Star Wars Show Halloween Scaretacular!",
      "link": "https://www.youtube.com/watch?v=EgpAsPYvRy0",
      "channel": {
        "name": "Star Wars",
        "link": "https://www.youtube.com/user/starwars",
        "verified": "true",
        "thumbnail": "https://yt3.ggpht.com/a-/AOh14GgskYzAhYn9cvahFlka1ODJVVGGvbJA4AGorw=s68-c-k-c0x00ffffff-no-rj-mo"
      },
      "published_date": "2 days ago",
      "views": 38469,
      "length": "11:37",
      "description": "This month on The Star Wars Show, we take a look back at The Mandalorian Season One, check out a brand new Star Wars: ...",
      "extensions": [
        "New"
      ],
      "thumbnail": {
        "static": "https://i.ytimg.com/vi/EgpAsPYvRy0/hq720.jpg?sqp=-oaymwEZCOgCEMoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLApJy8y6W9Hx90Ymdup5jrX_nXU8Q",
        "rich": "https://i.ytimg.com/an_webp/EgpAsPYvRy0/mqdefault_6s.webp?du=3000&sqp=CPee9fwF&rs=AOn4CLDd5RMlqSc3Wfp3jIWllwEyDU8FnQ"
      }
    }
  ]
}

def main():
    for titles, latest_from_star_wars in DATA.items():
        for titles in latest_from_star_wars:
            print(titles["title"],titles["length"])
    
    
    
    

if __name__ == '__main__':
    main()


    
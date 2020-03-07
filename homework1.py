name = "Sabina"
title = "UX"


if (len(name) % 2) == 1:
      print("+" + "-" * (len(name) + len(title)) + "+\n" +
            "|" + " " * (len(title) // 2) + name + " " * (len(title) // 2) + "|\n" +
            "|" + " " * (len(name) // 2) + title + " " * (len(name) // 2 + 1) + "|\n" +
            "+" + "-" * (len(name) + len(title)) + "+\n")
else:
      print("+" + "-" * (len(name) + len(title)) + "+\n" +
            "|" + " " * (len(title) // 2) + name + " " * (len(title) // 2) + "|\n" +
            "|" + " " * (len(name) // 2) + title + " " * (len(name) // 2) + "|\n" +
            "+" + "-" * (len(name) + len(title)) + "+\n")


if (len(title) % 2) == 1:
      print("+" + "-" * (len(name) + len(title)) + "+\n" +
            "|" + " " * (len(title) // 2) + name + " " * (len(title) // 2 + 1) + "|\n" +
            "|" + " " * (len(name) // 2) + title + " " * (len(name) // 2) + "|\n" +
            "+" + "-" * (len(name) + len(title)) + "+\n")
else:
      print("+" + "-" * (len(name) + len(title)) + "+\n" +
            "|" + " " * (len(title) // 2) + name + " " * (len(title) // 2) + "|\n" +
            "|" + " " * (len(name) // 2) + title + " " * (len(name) // 2) + "|\n" +
            "+" + "-" * (len(name) + len(title)) + "+\n")
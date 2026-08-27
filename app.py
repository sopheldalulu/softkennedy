from flask import Flask, render_template  # type: ignore[import-not-found]


class App(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_url_rule("/", view_func=self.home)
        self.add_url_rule("/about", view_func=self.about)
        self.add_url_rule("/projects", view_func=self.projects)

    def home(self):
        return render_template("index.html")

    def about(self):
        return render_template("about.html")

    def projects(self):
        return render_template("projects.html")


app = App(__name__)


if __name__ == "__main__":
    app.run(debug=True)
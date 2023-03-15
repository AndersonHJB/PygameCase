📦 setup.py (for humans)
=======================

这个代码库的存在是为了提供一个 [示例 setup.py] 文件，可用于启动您的下一个 Python 项目。它包括一些高级模式和最佳实践，适用于 `setup.py`，以及一些已注释掉的有用的功能。

> This repo exists to provide [an example setup.py] file, that can be used to bootstrap your next Python project. It includes some advanced patterns and best practices for `setup.py`, as well as some commented–out nice–to–haves.

例如，这个 `setup.py` 提供了一个 `$ python setup.py upload` 命令，它创建了一个 universal wheel（和 *sdist*），并使用 [Twine] 将您的包上传到 [PyPi]，而无需烦人的 `setup.cfg` 文件。它还自动创建/上传一个新的 git 标签。

> For example, this `setup.py` provides a `$ python setup.py upload` command, which creates a *universal wheel* (and *sdist*) and uploads your package to [PyPi] using [Twine], without the need for an annoying `setup.cfg` file. It also creates/uploads a new git tag, automatically.

简而言之，当您刚开始接触 `setup.py` 文件时，可能会感到令人生畏 — 即使 Guido 也曾听到过“每个人都在模仿别人的做法”。这是真的 — 所以，我希望这个代码库是最好的复制粘贴来源 :)

> In short, `setup.py` files can be daunting to approach, when first starting out — even Guido has been heard saying, "everyone cargo cults thems". It's true — so, I want this repo to be the best place to copy–paste from :)

[Check out the example!][an example setup.py]

Installation
-----

```bash
cd your_project

# Download the setup.py file:
#  download with wget
wget https://raw.githubusercontent.com/AndersonHJB/setup.py/main/setup.py -O setup.py

#  download with curl
curl -O https://raw.githubusercontent.com/AndersonHJB/setup.py/main/setup.py
```

To Do
-----

-   通过 `$ setup.py test` 运行测试（如果测试脚本很简洁的话）。

> Tests via `$ setup.py test` (if it's concise).

欢迎提交拉取请求！

> Pull requests are encouraged!

More Resources
--------------

-   [What is setup.py?] on Stack Overflow
-   [Official Python Packaging User Guide](https://packaging.python.org)
-   [The Hitchhiker's Guide to Packaging]
-   [Cookiecutter template for a Python package]

License
-------

这是一款自由和无拘束的软件，已发布到公共领域。

> This is free and unencumbered software released into the public domain.

任何人都可以自由复制、修改、发布、使用、编译、销售或分发该软件，无论是以源代码形式还是编译后的二进制形式，无论是用于商业或非商业目的，均可通过任何手段实现。

> Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

[an example setup.py]: https://github.com/AndersonHJB/setup.py/blob/main/setup.py
[PyPi]: https://docs.python.org/3/distutils/packageindex.html
[Twine]: https://pypi.python.org/pypi/twine
[image]: https://farm1.staticflickr.com/628/33173824932_58add34581_k_d.jpg
[What is setup.py?]: https://stackoverflow.com/questions/1471994/what-is-setup-py
[The Hitchhiker's Guide to Packaging]: https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html
[Cookiecutter template for a Python package]: https://github.com/audreyr/cookiecutter-pypackage

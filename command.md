# 1. 打包
- 更新 setuptools wheel

  ```
  python3 -m pip install --user --upgrade setuptools wheel
  ```

- 生成

  ```
  python3 setup.py sdist bdist_wheel
  ```

# 2. 上传

- 更新 twine

  ```
  python3 -m pip install --user --upgrade twine
  ```

- 上传到PyPi
  - 上传 PyPI
    
    ```
    python3 -m twine upload dist/*
    ```
    
  - 下载 PyPi
    
    ```
    pip install $your_package_name
    pip install $your_package_name -i https://pypi.python.org/simple/
    ```
  
- 上传到 test PyPi
  - 上传 test PyPI
    
    ```
    python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    ```
    
  - 下载 test PyPI
    
    ```
    python3 -m pip install --index-url https://test.pypi.org/simple/ $your_package_name
    ```
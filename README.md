logxstract
========================

Library for extracting xml from logs. Finds xml matching criteria and saves results to file.

## Install

```shell
$ pip install logxstract
```

## Example xml in log which could be extracted

![Example](https://user-images.githubusercontent.com/8684952/32408613-6471d374-c19b-11e7-9319-7d6416864010.png)


## Usage as library

```python

        from logxstract import extract_xml_from_file

        extract_xml_from_file(
            path='/item',
            body='/item',
            input_file='sample.log',
            output_file='result.txt'
        )
        #extracted xml is now in result.txt file
```

## Usage in shell

```shell
$ logxtract -p /item -b /item -f sample.log -o result.txt
```
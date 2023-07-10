from qqlabel import EdgeDetect, Convert

for i in range(58):
    detection = EdgeDetect(f'./sample/image_{i}.jpg')
    detection.detect()
    detection.save(f'./results/image/result_{i}.png')
    data = detection.output()

    convert = Convert(data)
    convert.create()
    convert.save(f'./results/json/result_{i}.json')



# mac-gyver

이것저것 기능을 가지고 있는 개인용 유틸리티 저장소

## main GUI

python + tkinter 로 제작 예정

## 콘솔 명령

기능을 콘솔 명령으로 나누어서 터미널로도 사용 가능하게 만들 예정
모듈로 분리하면 잘 되지 않을까 생각중

기본 사용법

```bash
fjdi.exe [대상 폴더 또는 파일] --명령 인자 ...
```

### 이미지 확대 또는 축소

이미지의 크기를 일괄 확대 또는 축소한다
업스케일링 기능을 넣을지 말지도 고민중

```bash
# fjdi [폴더이름] --resize <확대할 크기>
fjdi --resize 3 #현재폴더의 이미지들 3배 확대
fjdi ./images --resize 2
fjdi ./images --resize 0.5
# fjdid [폴더이름] --crop <변경할 크기>
fjdi ./images 
```

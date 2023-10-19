# mac-gyver

이것저것 기능을 가지고 있는 개인용 유틸리티 저장소

## 파이썬 모듈

- 주 용도는 API이므로 먼저 모듈로 제공해 줄 것

## CLI 기반 개발

- [Textual](https://textual.textualize.io/) 기반으로 UI 추가 예정
- https://textual.textualize.io/tutorial/


## 콘솔 명령

- pyinstaller를 이용해서 각각을 exe 파일로 만들고 texual로 연동하면 좋을 것 같다.

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

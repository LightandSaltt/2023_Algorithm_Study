# Stack (스택)
## Stack (스택)
Stack(스택)은 제한적으로 접근 할 수 있는 구조이다. 스택의 기본 원칙은 **'후입선출(LIFO : Last in First out)'** 이다. 또는 선입후출(FILO : First in Last out) 이라고도 한다. 보통 후입선출이라고 많이 표기한다. 말 그대로 '나중에 들어온 것이 먼저 나가는 방식'이다. 그림으로 보면 아래와 같다.
![](https://velog.velcdn.com/images/ygy0102/post/8e438a68-30a3-4d65-bec6-125615167d7a/image.png)

한쪽 에서만 원소를 넣거나 뺄 수 있는 자료구조이다. 프링글스 통을 생각하면 이해하기가 쉽다. 이러한 구조는 보통 **'뒤로 가기', '실행 취소(undo)', 컴퓨터 구조에서 'stack memory', '괄호검사', '재귀호출', 'DFS(깊이 우선 탐색)'** 등에서 쓰인다.

## Stack의 성질
>1. 원소의 추가는 O(1)
>2. 원소의 제거는 O(1)
>3. 제일 상단의 원소 확인 O(1)
>4. 제일 상단이 아닌 나머지 원소들의 확인/변경은 원칙적으로 불가능

(그러나 배열을 이용해 스택을 구현하면 기본적인 스택의 기능과 더불어 제일 상단이 아닌 나머지 원소들의 확인/변경을 가능 하도록 만들 수는 있다.)

## Stack 사용법
**선언**
```java
import java.util.Stack;

Stack<Integer> stack = new Stack<>();
```
**원소 추가**
```java
// Stack에 데이터 추가
stack.push(1);
stack.push(2);
```

**원소 추출**
```java
// Stack에서 데이터 추출
stack.pop();
```

**최상단 값 확인**
```java
// Stack의 최상단 값 출력 (제거는 이루어지지 않음)
stack.peek();
```
**메소드 정리**
>|메소드|설명|   
>|--|--|   
>|push()|데이터 추가|   
>|pop()|데이터 추출|   
>|peek()|최상단 값 확인|   
>|size()|현재 스택에 들어있는 데이터 개수 리턴|   
>|clear()|모든 데이터 삭제|   
>|empty()|스택이 비어있다면 true|   
>|contains()|특정 데이터가 포함되어 있는지|   
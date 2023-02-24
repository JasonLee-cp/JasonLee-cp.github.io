---
layout: post
title: "Ch4 - Program Structure and Execution"
subtitle: "운영체제와 정보기술의 원리 책을 공부하고 기록한 포스팅 입니다."
categories: dev
tags: os
comments:
---

"운영체제와 정보기술의 원리" 책 4장을 공부하고 기록한 글 입니다.

## 1. Program 구조와 interrupt

우리가 사용하는 컴퓨터 프로그램은 어떠한 언어로 작성되었든간에 그 내부 구조는 **function**으로 구성된다.

한편, 프로그램이 CPU에서 명령을 수행 하려면, 해당 instruction을 담은 프로그램의 **address space** (주소 영역)이 memory에 올라가 있어야 한다. 이떄 address space는 크게 다음 3개로 구분된다.

1. **code**
   - 우리가 작성한 프로그램 code들이 CPU에서 수행할수있는 machine instruction 형태로 변환되어 저장되는 부분
2. **data**
   - global variable 등 프로그램이 사용하는 data를 저장하는 부분
3. **stack**
   - function이 호출될 떄, 호출된 function을 마치고 복귀할 return address 및 데이터를 임시로 저장하는데 사용

우리가 작성한 program은 맨 처음 **main function**에서 실행을 시작해 main function이 다른 function A를 호출하면, "호출한 지점"을 stack에 저장해 놓았다가, A를 처리하고 stack에 저장된 return address로 돌아와 코드를 계속 수행한다.

즉, 함수가 호출되면 다음에 실행할 instruction의 memory 위치가 바뀌게 된다.

**Interrupt**의 동작 원리도 함수호출과 비슷하다. A라는 프로그램이 CPU를 할당받고 명령 수행중인데, interrupt가 발생하면 A는 현재 수행중인 명령의 위치를 **PCB**에 저장하고, interrupt service routine으로 넘어가서 처리를 하고 다시 돌아와 A의 이전 작업 지점부터 계석 수행한다.

일반적으로,

- 프로그램 내에서 발생되는 **function call** 에 필요한 return address는 각 프로그램의 address space 중 **stack**에 저장하고
- **Interrupt** 때문에 CPU를 빼앗긴 위치는 **PCB**에 저장된다.

## 2. Computer system의 동작 개요

CPU를 두뇌라고 하기에는 좀 그렇다..왜냐면 CPU는 "<span style="background:#fff88f">매 시점 memory의 특정 address에 존재하는 instruction을 하나씩 읽어와 그대로 실행</span>"하는 비~싼 장치일뿐이다. 이때, <span style="background:#fff88f">CPU가 수행해야할 memory address를 담고 있는 register</span>을 **PC(program counter)** 라고 한다. 즉, CPU는 매번 PC가 가리키는 memory address의 instruction을 고대~로 실행한다. 일반적으로 branching이나 loop가 없으면 PC는 next instruction을 가리켜 코드의 sequential execution이 이루어진다.

한편, <span style="background:#fff88f">computer system의 동작이 CPU에 의해서만 이루어지는것은 아니다</span>! Dis에서 파일을 읽어오기도 하고, 키보드로 입력을 받거나 모니터로 출력하는 등 다양하다.

<span style="background:#fff88f">Computer system을 구성하는 hardware</span>로는 먼저 **CPU**와 **memory**가 있다.

이 밖에, <span style="background:#fff88f">I/O device와 이들을 전담하는 작은 CPU와 메모리</span>가 있는데 이걸 **I/O controller**와 **local buffer**이라고 부른다.

> Memory에는 user program과 OS가 같이 올라가 수행된다

<span style="background:#fff88f">Memory에는 user program만 올라가는게 아니라, OS도 같이 올라가서 수행</span>된다. 이떄, CPU는 항상 <span style="background:#fff88f">PC가 가리키는 memory address의 instruction을 수행</span>한다. 그럼 PC가 뭐를 가리키냐에 따라 user program이냐 OS 코드냐가 정해지겠죠?

- PC가 <span style="background:#fff88f">OS가 존재하는 부분을 가리키고 있다면</span>, OS code를 수행 중이며, 이 경우 CPU가 **kernel mode**에서 수행 중이라고 한다.
- PC가 <span style="background:#fff88f">user program이 존재하는 부분을 가리키고 있다면</span>, **user mode**에서 CPU가 수행되고 있다고 얘기를 한다.

> Normal operation vs Privilege operation

CPU가 수행하는 명령에는 **normal opereation**과 **privilege operation**이 있다

**Normal operation**은 <span style="background:#fff88f">1) memory에서 데이터를 읽어와</span>, <span style="background:#fff88f">2) CPU에서 어떤 계산을 하고</span>, <span style="background:#fff88f">3) 다시 memory에 쓰는</span> 일련의 명령들을 말한다. 이런 명령들은 모든 프로그램이 수행할수있다.

**Privilege operation**은 <span style="background:#fff88f">보안이 필요한 명령</span>으로 I/O, timer 등 <span style="background:#fff88f">각종 device에 접근하는 명령</span>이다. 이러한 privilege operation은<span style="background:#fff88f"> 항상 OS만이 수행</span>할 수 있도록 제한하고 있다.

이러한 두 operation을 체크하기 위해 **mode bit**라는걸 둔다.

<span style="background:#fff88f">User program</span>이 실행되다 보면 normal operation외에 <span style="background:#fff88f">privilege operation</span>이 필요한 경우가 있다. 예를들어, <span style="background:#fff88f">I/O에 접근</span>한다거나, <span style="background:#fff88f">disk의 file</span>에 접근한다거나, 결과를 모니터에 출력하는 등의 작업을 할때는, **system call**을 통해 OS에 대행을 맡긴다.

User program이 syscall을 하게 되면 <span style="background:#fff88f">OS는 kernel space에 정의된 system call 처리 코드를 수행</span>하게 된다. 예를들어, disk에서 자료를 읽어오는 syscall이라면,

1. CPU가 <span style="background:#fff88f">disk controller</span>에게 data를 읽어오라는 명령을 내린다.
2. Disk controller는 disk로부터 데이터를 읽어와서, <span style="background:#fff88f">local buffer</span>에 저장한다.
3. 다 저장했으면 controller는 CPU에 <span style="background:#fff88f">interrupt</span>를 발생시켜서 I/O가 완료되었음을 알린다.

CPU는 PC가 가리키는 memory address의 instruction만 계속 수행하기 때문에 external device 상태를 지속적으로 파악할 수 없다. 따라서 주변장치들은 CPU의 도움이 필요한 경우 <span style="background:#fff88f">interrupt</span>를 사용해 CPU에게 서비스를 요청한다. Interrupt를 발생시키기 위해 주변장치는 <span style="background:#fff88f">interrupt line</span>을 세팅하고, <span style="background:#fff88f">CPU는 매번 명령을 수행한 "직후" interrupt line을 체크</span>해 서비스 요청이 들어왔는지 확인한다. Interrupt가 발생하면 CPU는 해당 interrupt를 처리하기 위한 <span style="background:#fff88f">interrupt service routine</span>으로 이동해서 kernel내의 처리 코드를 수행한다

[Note] 이때, interrupt의 종류는 다양하기 때문에 각각의 interrupt 원인마다 line을 다르게 해서 구분하게 된다.

---

## 3. Program Execution

프로그램이 실행되고 있다 (program in execution)란 말은 <span style="background:#fff88f">두가지 중요한 의미</span>를 가진다.

1. <span style="background:rgba(240, 107, 5, 0.2)">Disk에 존재하던 file이 memory에 적재</span>된다는 의미
2. <span style="background:rgba(240, 107, 5, 0.2)">프로그램이 CPU를 할당받고 instruction을 수행하고 있는 상태</span>라는 의미

실행파일이 memory에 적재될때, 전체가 memory에 한꺼번에 올라가는거 보단 <span style="background:#fff88f">일부분만 memory에 올라가고, 나머지는 disk의 swap area</span>에 내려놓는것이 일반적이다.

> **Process Address Space**

Process의 address space는 크게 **code**, **data**, **stack** 등으로 구성된다. <span style="background:#fff88f">각각의 process마다 이러한 address space를 별도로 가지며</span>, 프로그램마다 독자적으로 존재하는 이와 같은 address space를 우리는 **virtual memory** (또는 logical memory)라고 부른다. 이는 실제 physical memory와는 독립적으로 각 프로그램마다 독자적인 address space를 가지기 때문에 부르는 말이다.

> **OS도 하나의 프로그램이기 때문에 kernel 역시 code, data, stack과 같은 address space를 가진다.**

OS의 기능이 <span style="background:#fff88f">(1) 아랫단의 hardware resource를 효율적으로 관리</span> <span style="background:#fff88f">(2) application 및 user에게 편리한 interface를 제공</span> 하는 것이므로, kernel의 코드는

1. <span style="background:#fff88f">CPU, memory 등의 자원을 관리하기 위한 부분</span>과
2. <span style="background:#fff88f">user에게 편리한 interface를 제공하기위한 부분</span>이 주를 이루고 있다.
3. 이 밖에도 kernel의 code는 <span style="background:#fff88f">s</span><span style="background:#fff88f">ystem call 및 interrupt를 처리하기 위한 부분</span>을 포함한다.

> **Kernel의 data 영역**

<span style="background:#fff88f">Kernel의 data 영역에는 각종 resource를 관리하기 위한 data structure이 저장</span>된다. CPU나 memory와 같은 <span style="background:#fff88f">hardware resource를 관리하기 위한 data structure</span> 뿐만 아니라, 현재 수행중인 <span style="background:#fff88f">program을 관리하기 위한 data structure도 저장</span>된다.

이때, program in execution을 **process**라고 하고, kernel의 데이터 영역에는 각 <span style="background:#fff88f">process 의 status, CPU 사용 정보, memory 사용 정보 등을 유지하기 위한</span> data structure인 **PCB**를 두고 있다.

> **Kernel의 stack 영역**

Kernel의 stack 영역은 일반 프로그램의 stack과 마찬가지로, <span style="background:#fff88f">function call시에 return address를 저장하기 위한 용도</span>로 사용된다.

하지만, <span style="background:#fff88f">kernel의 stack은 일반 user program stack과 달리, 현재 수행 중인 process 마다 "별도로" stack을 두어 관리</span>한다.

<span style="background:rgba(136, 49, 204, 0.2)">WHY?</span>

1. Process가 function call을 할때 자신의 address space안에 정의된 function을 호출하면 자신의 stack에 return address를 저장하지만, process가 <span style="background:#fff88f">privilege operation</span>을 수행하려고 1) **kernel에 정의된 syscall을 호출**하고, 2) **syscall "내부에서" 다른 function call**을 할 경우, 그 <span style="background:#fff88f">return address는 kernel 내의 주소</span>가 되어, user program stack과는 별도의 저장공간이 필요하게 된다.
2. 또한, kernel은 일종의 <span style="background:#fff88f">shared code</span> 로서, 모든 user program이 syscall을 통해 kernel의 function에 접근할 수 있으므로, 일관성 유지를 위해 각 process마다 별도의 kernel stack을 두게 되는 것이다.

정리하자면, program이 <span style="background:#fff88f">자기 자신의 코드내에서 function call을 할때는 자신의 address space안에 있는 stack</span>을 사용하고, <span style="background:#fff88f">system call이나 interrupt 등으로 OS code가 "실행되는 와중에" function call이 발생할 경우에는 kernel stack</span>을 사용하게 되는 것이다

<span style="background:#ff4d4f">[WARNING]</span> Program내의 함수 호출 시, 해당 프로그램의 stack에 return address를 저장하지만, syscall이나 interrupt 발생으로 "**CPU의 수행 주체가 OS로 바뀌는 순간**"에는 직전에 수행되던 program의 return address를 stack이 아닌 **PCB**에 저장한다. 좀 헷갈릴수 있는이렇게 생각하자. <span style="background:#fff88f">"CPU가 OS로 넘어갈때(syscall, interrupt, etc)"는 PCB에 저장</span>하고, <span style="background:#fff88f">"kernel code가 수행되는 도중에 이루어지는 function call"은 kernel stack을 사용</span>하게 되는 것이다.

<span style="background:#fff88f">Kernel stack은 process마다 별도</span>로 두고 있어, kernel 내에서 이루어지는 function call은 직전에 CPU를 가지고있던 process의 kernel stack을 사용한다.

---

## 4. User program이 사용하는 function

프로그램이 사용하는 함수는 크게 3가지로 나눌 수 있다.

1. **User defined function**
   - 프로그래머가 직접 작성한 함수
2. **Library function**
   - 이미 누군가 작성해놓은 함수를 호출만 하여 사용
3. **Kernel function**
   - OS kernel의 code에 정의된 함수
   - <span style="background:rgba(136, 49, 204, 0.2)">system call</span>: user program이 OS 서비스를 요청하기 위해 호출하는 함수
   - <span style="background:rgba(136, 49, 204, 0.2)">Interrupt service routine</span>: 각종 hardware 및 software이 CPU의 서비스를 요청하기 위해 발생시키는 함수

**User defined function**과 **library function**은 모두 그 <span style="background:#fff88f">프로그램의 code area에 machine instruction 형태로 존재</span>하며, 프로그램이 실행될때 해당 <span style="background:#fff88f">process의 address space공간에 포함</span>된다. 또한, 함수 호출 시에도 <span style="background:#fff88f">자신의 address space에 있는 stack</span>을 사용한다

반면, **kernel function**은 <span style="background:#fff88f">OS kernel의 code에 정의된 함수</span>를 뜻하며, user program의 address space에 저장되는게 아니라, <span style="background:#fff88f">kernel의 address space에 코드가 정의</span>된다.

OS 내에는 syscall 함수로 `read()`와 `write()` 함수가 정의돼 있으며, 각각 input, output을 필요로 할때 호출하는 함수다.

System call은 OS라는 별개의 프로그램에 CPU를 넘겨서 실행하는 것이다. CPU를 OS에 넘기기 위해 <span style="background:#fff88f">syscall은 interrupt가 동일한 메커니즘, 즉 CPU의 interrupt line을 세팅</span>하는 방법을 사용한다.

## 5. Interrupt

CPU는 특별한 일이 없으면 현재 수행중인 process의 next instruction을 순차적으로 수행한다. CPU는 PC가 가리키는 곳에 있는 instruction을 수행하는데, 매 명령을 수행하고 나서, **interrupt line**이 세팅 되어있는지를 체크한다. Interrupt가 발생했으면, CPU는 현재 수행하던 process를 멈추고 **interrupt service routine**으로 이동해서 인터럽트 처리를 수행한다. 마치고 나면 interrupt가 발생하기 직전의 process에게 CPU control을 넘겨준다.

> **Interrupt 처리 중에 또 다른 interrupt가 발생한다면?**

<span style="background:#fff88f">원칙적으로는 interrupt 처리 중에 또 다른 interrupt가 발생하는것을 허용하지 않는다</span>. 왜냐하면 <span style="background:#fff88f">데이터의 일관성이 유지되지 않는 문제</span>가 발생할수있기 때문이다. Interrupt를 처리하는 중에 OS에 정의된 data를 변경하고 있는데, 다른 interrupt가 발생해 앞선 interrupt에서 변경 중이던 데이터를 또 다시 변경하게 되면 의도하지 않았떤 결과값이 나올수 있기 때문이다.

하지만! <span style="background:#fff88f">현재 인터럽트보다 더 시급하거나 CPU를 당장 사용해야 하는 일</span>이 발생할 수 있다. 이 경우에는 <span style="background:#fff88f">상대적으로 낮은 중요도를 가진 interrupt</span>를 처리하는 도중에 <span style="background:#fff88f">중요도가 더 높은 interrupt</span>가 들어오면, 현재 interrupt 코드 수행 지점을 저장하고, <span style="background:#fff88f">우선순위가 높은 interrupt를 처리하게 된다. </span>

## 6. System call

모든 프로그램은 자신만의 독자적인 **address space**를 가지고 있다. <span style="background:#fff88f">System call</span>은 함수호출이기는 하지만 자신의 address space밖에 있는,<span style="background:#fff88f"> kernel의 address space에 존재하는 함수</span><span style="background:#fff88f">를 호출</span>한다.

일반적으로 function call이 자신의 stack에 return address를 저장하고 호출된 functionㅇ의 위치로 점프하는것과 달리, <span style="background:#fff88f">syscall은 "프로그램 자신이 직접" interrupt line에 interrupt을 세팅하는 명령</span>을 통해 이루어진다. 이는 프로그램이 직접 인터럽트 라인 셋팅하는것만 다를 뿐, 일반적인 interrupt와 동일한 방법이다.

Ex) <span style="background:#fff88f">Disk file I/O</span>를 생각해보자. User program이 CPU에서 명령을 수행하던 중, disk에서 file read를 해야 할 경우, syscall로 kernel의 function을 호출하게 된다. 이때, 프로그램은 <span style="background:#fff88f">i</span><span style="background:#fff88f">nterrupt line을 세팅</span>하고, CPU는 다음 명령 수행전에 인터럽트 라인이 세팅되어있는걸 확인하고, 현재 user program을 멈춘 후, CPU control을 OS로 넘기게 된다. 그러고 <span style="background:#fff88f">service routine</span>으로 이동해 CPU는 <span style="background:#fff88f">disk controller에게 파일을 읽어오라는 명령</span>을 내린다.

이떄, disk controller가 <span style="background:#fff88f">디스크에서 데이터를 읽어오는것은 상대적으로 많은 시간</span>이 걸리기 때문에, CPU가 I/O의 완료를 기다리고만 있을순 없기 때문에, <span style="background:#fff88f">OS가 I/O request를 한 다음 다른 process에게 CPU control을 이양</span>한다. 다른 process가 CPU에서 명령을 수행하던 중 I/O가 완료되면 disk controller가 CPU에게 interrupt를 발생시켜, I/O 작업을 끝났음을 알린다. 그러면, CPU는 user program을 잠시 멈추고, service routine으로 CPU control이 넘어간다. 이때 발생한 interrupt는 **hardware interrupt**에 해당되며 그 내용은 disk로부터 local buffer로 읽어온 내용을 memory로 복사한후 disk I/O를 요청했던 process에게 다시 **CPU를 획득할수있는 권한**을 주는 것이다. 그러면, 해당 process는 **ready queue**에 삽입된다.

지금까지 살펴본 내용을 보면, 프로그램이 CPU를 할당받고 명령을 하다가 중간에 CPU를 빼앗기는 경우는 크게 두가지다.

1. **Timer interrupt**
2. **I/O를 위한 System call**

---

## 7. Process의 두가지 실행 상태

하나의 process가 시작되어 완료되기까지는 <span style="background:#fff88f">process 자신의 address space에 있는 코드</span>만 실행되는게 아니라, <span style="background:#fff88f">kernel의 address space에 있는 코드</span>도 실행된다. 이는 user-defined function뿐만 아니라, <span style="background:#fff88f">syscall등을 통해 kernel function도 호출</span>하기 때문이다.

1. **user mode running**
   - 자신의 address space에 정의된 코드를 실행
2. **kernel mode running**
   - kernel의 syscall 함수를 실행

[NOTE] 비록 syscall을 통해 실행되는것이 process의 코드가 아닌 OS kernel code이긴 하지만, 우리는 <span style="background:#fff88f">syscall이 수행되는동안</span> 여전히 **process가 running state다**라고 말한다. 왜냐면 kernel code가 사실상 process가 해야할일을 대행해주는 것이기 때문이다.

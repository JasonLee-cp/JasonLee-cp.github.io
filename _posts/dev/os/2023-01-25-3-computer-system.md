---
layout: post
title: "Ch3 - Computer system의 동작 원리"
subtitle: "운영체제와 정보기술의 원리 책을 공부하고 기록한 포스팅 입니다."
categories: dev
tags: os
comments:
---

"운영체제와 정보기술의 원리" 책 3장을 공부하고 기록한 글 입니다.

## 1. Computer system organization

컴퓨터 시스템의 구조는 (1)**internal device**인 CPU, memory와 (2)**external device**인 disk, keyboard, monitor, network device, etc 로 구성된다

컴퓨터는 <span style="background:#fff88f">external device에서 internal device로 데이터를 읽어와 각종 연산을 수행하고, 그 결과를 다시 external device로 내보내는 방식</span>으로 업무를 처리한다. 이런 행위를 <span style="background:#fff88f">I/O</span>라\*\*\*\*고 한다.

<font color="#ff0000">[TIP]</font> disk도 external device 이므로, disk에서 내용을 읽어 컴퓨터 내부에서 연산을 한후 disk에 데이터를 저장한다면, 컴퓨터 입장에서는 역시 I/O가 일어난 것이다.

<span style="background:rgba(136, 49, 204, 0.2)">Controller</span>
memory 및 I/O device 등의 각 hardware device에는 **controller**이라는 것이 붙어 있다.
컨트롤러는 <span style="background:#fff88f">일종의 작은 CPU</span>로서, 각 <span style="background:#fff88f">hardware device마다 존재</span>하며 이들을 "제어"하는 작은 CPU라고 해석하면 된다.

예를들어, memory를 제어하는 controller은 <span style="background:#fff88f">memory controller</span>이고, disk를 제어하면 <span style="background:#fff88f">disk controller</span>이다.

---

## 2. CPU 연산과 I/O 연산

I/O 장치들의 연산은 **I/O controller**가 담당하고, 컴퓨터 내에서 수행되는 연산은 **CPU**가 담당한다. 이때, I/O device와 CPU는 동시 수행이 가능하다.

한편, 각 device마다 이를 제어하기 위해 설치된 device controller라는 장치로부터 <span style="background:#fff88f">들어오고 나가는 data를 temporary save하기 위해 작은 memory</span>를 가지고 있는데, 이를 **local buffer**이라고 한다. Disk나 keyboard 등에서 data를 읽어오는 경우, <span style="background:#fff88f">우선 local buffer에 data를 임시로 저장된 후, memory에 전달</span>된다. 이때, <span style="background:#fff88f">device에서 local buffer로 읽어오는 일은 controller가 담당</span>한다.

예를들어, program B가 수행 중에 disk에서 데이터를 읽어오라는 명령을 내리면, disk controller가 physical disk에서 내용을 읽어 이를 local buffer에 저장한다. 원하는 데이터를 local buffer으로 다 읽어오면 B는 CPU에서 다음 일을 수행한다.

이때, local buffer로 읽어오는 작업이 끝났는지를 CPU가 계속 체크하는게 아니라, <span style="background:#fff88f">device controller가 interrupt을 발생시켜 CPU에 보고</span>하게 된다.

기본적으로 CPU는 매 시점 memory에서 instruction을 하나씩 읽어와서 수행한다. 이때, CPU 옆에는 **interrupt line**이 있다. CPU는 instruction하나를 수행할 때마다 interrupt가 발생했는지를 interrupt line에 신호가 들어왔는지를 확인하고 들어왔으면 interrupt를 처리하러 간다.

interrupt는 CPU에 알려줄 이벤트가 일어난 경우 <span style="background:#fff88f">controller가 발생</span>시킨다.

---

## 3. Interrupt의 일반적 기능

<span style="background:#fff88f">Kernel에는 interrupt가 들어왔을 때 해야 할일이 미리 다 programming되어 그 코드가 보관</span>되어 있다. 그 중 한가지가 **interrupt service routine**(or **interrupt handler**)이다. Interrupt service routine은 <span style="background:#fff88f">다양한 interrupt에 대해 각각 처리해야 할 업무들을 정의</span>한다.

예를 들어, disk controller가 interrupt를 발생시키면, CPU는 하던 일을 멈추고 이 interrupt가 발생했을때 처리해야되는 코드를 찾아 수행한다. 이때 수행하는 일은, disk의 local buffer에 있는 내용을 memory로 전달하고, 해당 프로그램이 CPU를 할당받을 경우, 다음 instruction을 수행할 수 있음을 표시해두는 일이다.

> **Hardware interrupt** vs **Software interrupt**

Interrupt에는 hardware interrupt와 software interrupt가 있다. CPU의 서비스가 필요한 경우, CPU 옆에 있는 interrupt line에 신호를 보내 interrupt가 발생했음을 방식은 동일하다.

다른점은,

<span style="background:rgba(136, 49, 204, 0.2)">hardware interrupt</span>: controller 등 <span style="background:#fff88f">hardware device가 CPU의 interrupt line을 셋팅</span>
<span style="background:rgba(136, 49, 204, 0.2)">software interrupt</span>: <span style="background:#fff88f">software가 그 일을 수행</span>

> **Interrupt vector**

OS는 할 일을 쉽게 찾아가기 위해 interrupt vector를 가지고 있다. Interrupt vector란, <span style="background:#fff88f">interrupt 종류마다 번호를 정해서, 번호에 따라 처리해야 할 코드가 위치한 부분을 pointing하는 data structure</span>을 말한다.

<span style="background:#fff88f">실제 처리해야 할 코드는 interrupt service routine</span> 또는 Interrupt handler이라고 불리는 다른 곳에 있다.

## 4. Interrupt handling

**Interrupt handling** 이란, <span style="background:#fff88f">interrupt가 발생한 경우에 처리해야 할 일의 절차</span>를 의미한다.

Program A가 실행되고 있을때, interrupt가 발생하면 A의 실행 중이던 코드의 <span style="background:#fff88f">memory address</span>, <span style="background:#fff88f">register values</span>, <span style="background:#fff88f">hardware status</span>, 등등을 **PCB (process control block)** 에 저장한 후, <span style="background:#fff88f">CPU control이 interrupt service routine</span>으로 넘어간다. Interrupt 처리가 끝나면, 저장된 상태를 PCB로부터 CPU상에 restore해 interrupt 당하기 직전의 위치부터 실행이 된다.

오늘날의 컴퓨터에서, <span style="background:#fff88f">OS는 interrupt가 발생할 때에만 실행</span>된다! CPU는 항상 user program에 의해 사용되며, interrupt가 발생했을 경우에만 CPU의 제어권을 획득할 수 있다.

## 5. I/O 구조

I/O란 컴퓨터 시스템이 외부 I/O device들과 데이터를 주고받는것을 말한다. I/O 방식에는 **synchronous I/O**와 **asynchronous I/O**가 있다.

> **Synchronous I/O (동기식 입출력)**

<span style="background:#fff88f">어떤 프로그램이 I/O 요청을 했을 때, I/O 작업이 완료된 후에야 그 프로그램이 후속 작업을 수행할 수 있는 방식</span>을 말한다.

따라서, synchronous I/O에서 <span style="background:#fff88f">CPU는 I/O operation이 끝날 때까지 interrupt를 기다리며 resource를 낭비</span>하게 된다. CPU의 명령 수행 속도는 빠르지만 <span style="background:#fff88f">I/O 연산은 상대적으로 느리다</span>. 그럼에도 불구하고 I/O가 끝날때까지 기다렸다가 user program에 CPU control을 넘기는건 자원의 낭비를 초래하게 된다.

따라서, 일반적으로 프로그램이 I/O를 수행중인 경우, <span style="background:#fff88f">CPU를 다른 프로그램에게 transfer해 CPU가 쉬지않고 일할수 있도록 관리</span>한다. 이를 관리하기 위해, 입출력 중인 프로그램을 **blocked state**로 전환시킨다.

어떤 프로그램이 synchronous I/O를 수행 중일때, CPU를 다른 프로그램에 할당하지 않는다면 매 시점 하나의 I/O 연산만 수행될 수 있기 때문에 synchronization은 자동적으로 이루어진다.

하지만, I/O가 수행중일떄 다른 프로그램에게 CPU를 transfer하게 되므로, <span style="background:#fff88f">다수의 입출력 연산이 동시에 요청되거나 처리</span>될 수 있다. 예를들어,

program A: disk에 원래 1이던 file의 내용을 3으로 바꾸는 I/O operation
program B: disk에 원래 1이던 file의 내용을 1 증가시키는 I/O operation

이때, program A -> program B 순서대로 실행되는게 목표인데, I/O 연산을 수행중이던 A에게서 CPU를 빼앗아 B에 transfer을 하면, `1 -> 3-> 4` 가 아니고 `1 -> 2 -> 3` 이 되어 의도하지 않은 결과를 초래할수 있다.

따라서, synchronous I/O에서는 I/O request의 <span style="background:#fff88f">synchronization을 위해 device별로 queue를 두어, 요청한 순서에 따라 처리</span>할 수 있도록 한다.

![](/assets/img/os/os3_1.png)

위의 그림처럼 device마다 **queue header**이 존재한다. <span style="background:#fff88f">Controller는 이 순서에 따라 매 시점 하나씩 I/O 작업을 처리</span>하게 된다. 이때, CPU에 비해서 controller의 수행속도나 device 자체의 작업 수행 능력은 매우 떨어진다. 그러므로, I/O가 완료될때까지 CPU가 노는게 아니라, <span style="background:#fff88f">I/O와 관련없는 프로그램을 수행</span>하도록하고, 요청된 I/O 연산이 완료되면, CPU에게 <span style="background:#fff88f">interrupt를 통해서 I/O작업이 완료됐다고 알려준다</span>. 이 경우 kernel은 interrupt service routine으로 가서, I/O 연산을 끝낸 프로그램이 CPU를 할당 받을 수 있도록 그 프로그램의 상태를 ready로 바꾸게 된다.

> **Asynchronous I/O**

<span style="background:#fff88f">I/O 연산을 요청한 후에 끝나기를 기다리지않고 CPU control을 연산을 호출한 그 프로그램에게 곧바로 다시 부여하는 방식</span>을 말한다.

예를들어, 어떤 프로그램이 disk에서 데이터를 읽어오라는 요청을 했을때, 보통은 읽어온 결과를 이용해서 다음 연산을 하지만, <span style="background:#fff88f">때에 따라선 그 데이터와 관련없는 작업을 수행</span>할수 있다. Asynchronous I/O에서는 그러한 작업을 먼저 수행하고, 읽어오는 데이터가 반드시 있어야 수행할수있는 일들은 I/O가 끝난뒤에 한다. 또한 disk에 읽어오는게 아니라 그냥 <span style="background:#fff88f">write</span>하는 경우여도 작업이 완료되기 전에 다음 명령을 수행할수있으므로 asynchronous I/O가 사용될수 있다.

> **Synchronous vs Asynchronous Recap**

![](/assets/img/os/os3_2.png)

User program이 I/O request를 하면,

**Synchronous I/O**에서는 먼저 kernel으로 CPU control이 넘어와서, I/O 처리와 관련된 kernel의 코드가 실행된다. 이떄, I/O를 호출한 process를 <span style="background:#fff88f">blocked state</span>로 바꾸어 I/O가 완료될때까지 CPU를 할당받지 못한다. <span style="background:#fff88f">I/O가 완료되면 I/O controller가 interrupt</span>를 발생시켜 CPU에게 I/O가 완료됐음을 알려주고, 이 process를 <span style="background:#fff88f">ready state</span>로 바꾸어서 CPU를 할당받을 수 있는 권한을 준다.

**Asynchronous I/O**에서는, CPU control을 <span style="background:#fff88f">I/O를 요청한 process에게 "곧바로 다시" 주어지며</span>, I/O 연산이 완료되는 것과 무관하게 처리 가능한 작업부터 처리한다. 한편, async I/O에서도 I/O가 완료되면 interrupt를 통해 CPU에게 알려준다.

> Example

1. Program A가 disk에서 어떤 데이터를 읽어오는 instruction을 만나면, <span style="background:#fff88f">system call</span>을 통해 CPU에게 일종의 <span style="background:#fff88f">software interrupt</span>를 발생시킨다
2. CPU는 A의 코드 실행을 멈추고, 현재의 context를 저장한 후, interrupt에 의해 처리해야 할 kernel의 <span style="background:#fff88f">routine</span>으로 이동한다.
3. interrupt service routine으로 이동하면, CPU는 controller에게 I/O operation을 요청한다.
4. Controller는 A가 요청한 데이터를 disk로부터 자신의 <span style="background:#fff88f">local buffer</span>로 읽어온다. 읽어오는 동안에 A는 CPU를 다시 할당받지 못하게 된다.
5. OS는 A가 I/O를 요청했으므로, <span style="background:#fff88f">blocked state</span>로 바꾼다. 그리고 다른 프로그램 B에게 할당해 계속 CPU가 일을 할수있게 한다.
6. 원하는 정보가 local buffer로 다 들어오면 controller는 CPU에게 interrupt를 발생시켜 CPU에게 알린다. (이때는 <span style="background:#fff88f">hardware interrupt</span> - 컨트롤러가 했으니까)
7. B를 수행중이던 CPU는 B의 context를 저장하고 interrupt를 처리하러 가자~ interrupt service routine은 local buffer에 있는 A가 요청한 데이터를 A의 <span style="background:#fff88f">memory space</span>으로 읽어오고, A를 ready state로 바꾼다
8. 그 후, 다시 B로 돌아가서 업무를 계속 수행한다

---

## 6. DMA

원칙적으로 <span style="background:#fff88f">memory는 CPU에 의해서만 접근할 수 있는 device</span>이다.

따라서, <span style="background:#fff88f">CPU외의 device</span>가 memory의 data에 접근하려면 CPU에게 <span style="background:#fff88f">interrupt를 발생시켜 CPU가 대행</span>해주는 방식으로만 가능하다. Controller가 CPU에게 interrupt를 발생시키면, CPU는 <span style="background:#fff88f">controller local buffer</span>과 <span style="background:#fff88f">memory</span>사이에서 데이터를 옮긴다.

하,,지만... 모든 memory access가 CPU에 의해서만 이루어지면, <span style="background:#fff88f">CPU가 interrupt에 의해 너무 많은 방해</span>를 받기 때문에, 이런 비효율성을 극복하기 위해 "<span style="background:#fff88f">CPU 이외에 memory access가 가능한 device</span>"를 하나 더 두는 경우가 많은데, 이를 **DMA(Direct Memory Access)**라고 한다.

<span style="background:#fff88f">DMA는 일종의 controller</span>로서, CPU가 I/O device들의 memory access에 의해 자주 interrupt당하는것을 막아주는 역할을 한다. <span style="background:#fff88f">DMA는 local buffer에서 memory로 읽어오는 작업을 CPU대신 대행</span>함으로써 효율성을 높여준다.

DMA는 byte단위가 아니라 **block**이라는 <span style="background:#fff88f">"큰 단위"</span>로 정보를 memory로 읽어온 후에, CPU에게 interrupt를 발생시켜 해당 작업의 완료를 알려준다.

## 7. Storage의 구조

컴퓨터 시스템을 구성하는 storage는 **main memory**와 **secondary storage**로 나뉜다.

Main memory는 보통 memory라고 부르며, 전원이 나가면 저장되었던 내용이 모두 사라져버리는 **volatile**(휘발성)의 <span style="background:#fff88f">RAM을 매체로 사용</span>하는 경우가 대부분ㄴ이다.

Secondary storage는 전원이 나가도 저장된 내용을 기억하는 <span style="background:#fff88f">nonvolatile</span>(비휘발성)의 magnetic disk를 주로 사용한다. 이 외에도, flash memory, CD, magnetic tape 등이 있다.

> Secondary storage의 두가지 용도

1. **File system**
   - 전원이 나가도 유지해야할 정보를 저장한다
2. **Swap area** (memory의 연장 공간)
   - Memory는 크기가 한정되고 비싼데다가 용량이 작아서, multiple program이 메모리에 올라가 동시에 수행되는 현대의 컴퓨터에서는 memory space가 부족한 경우가 많다.
   - 따라서, OS는 프로그램에 <span style="background:#fff88f">당장 필요한 부분만 memory에 옮기고 그렇지 않은 부분은 disk의 swap area</span>에 내려놓는다. 이처럼 disk에 내려놓는 일을 **swap out**시킨다고 말하며, 필요할떄 다시 memory에 불러 들인다.
   - Swap area로는 hard disk가 가장 널리 사용된다.
   - Hard disk에는 여러 개의 magentic 원판들이 있고, arm, track, sector등으로 구성된다. sector에 최소 단위 정보가 저장된다.

---

## 8. Memory Hierarchy

![](/assets/img/os/os3_3.png)

컴퓨터 시스템을 구성하는 storage device는 "<span style="background:#fff88f">빠른 저장장치</span>"와 "<span style="background:#fff88f">느린 저장장치</span>"까지 hierarchical organizaiton으로 이루어진다.

**Register**, **cache**, **main memory**와 같은 빠른 저장장치는 <span style="background:#fff88f">가격이 높기</span> 때문에 <span style="background:#fff88f">적은 용량</span>을 사용하며 <span style="background:#fff88f">volatile</span>이다.

**Hard disk**, **magnetic disk** 등 느린 저장장치는 <span style="background:#fff88f">가격이 싸지만</span> <span style="background:#fff88f">느리고</span>, <span style="background:#fff88f">nonvolatile</span>이다.

<span style="background:#fff88f">상위 hierarchy로 갈수록 접근속도가 월등히 빠르지만 용량이 상대적으로 적다</span>. 하지만, <span style="background:#fff88f">당장 필요한 정보만을 선별적으로 저장</span>하면 큰 용량의 storage를 가지고 있는것과 비슷한 성능을 낼 수 있다. 예를들어, 상대적으로 용량이 적은 빠른 저장장치를 이용해 느린 저장장치의 성능을 향상시키는 기법인 <span style="background:#fff88f">caching</span>처럼, 당장 사용되거나 빈번히 필요한 정보를 저장해두는 것이다.

## 9. Hardware 보안

흔히 OS에는 <span style="background:#fff88f">multi-programming</span> 환경에서 동작한다. 그러므로, 각 프로그램이 다른 프로그램의 실행을 방해하거나 서로간의 충돌을 일으키는 문제를 막기 위해 **하드웨어에 대한 보안기법**이 필요하다.

Hardware security를 유지하기 위해 OS는 기본적으로 **kernel mode** (혹은 <span style="background:#fff88f">system mode</span>)와 **user mode**를 지원한다.

중요한 정보에 접근해 위험한 상황을 초래할 수 있는 연산은 **kernel mode**에서만 실행되도록한다. Kernel mode에서는 OS가 CPU control을 가지고, OS code를 실행하는 모드로서, <span style="background:#fff88f">모든 instruction을 다 실행</span>할 수 있다.

한편 **user mode**에서는, 일반 <span style="background:#fff88f">user program</span>이 실행되며, <span style="background:#fff88f">limited operations</span>만 실행할 수 있다.

하지만 OS가 user program이 딴짓하는지 어떻게 감시할까? 이를 위해 하드웨어적인 지원이 필요한데, CPU 내부에 **mode bit**를 두어, user program을 감시하게 된다.

- Mode bit **0**: **kernel mode**
- Mode bit **1**: **user mode**

<span style="background:#fff88f">CPU는 보안과 관련된 instruction을 수행하기 전에는 항상 mode bit가 0인지 확인</span>한다. 그리고 OS가 user program에게 CPU control을 넘길때는 <span style="background:#fff88f">mode bit를 1로 셋팅해 넘긴다</span>. User program이 하드웨어 접근 등 중요한 명령을 수행해야 할떄는 **system call**을 통해 OS에게 대행을 요청한다. <span style="background:#fff88f">Interrupt가 발생할때 mode bit는 자동으로 0으로 세팅</span>되고, OS가 요청된 작업이 모두 <span style="background:#fff88f">끝내면 mode bit를 다시 1로 만들어 user program</span>에 넘겨준다.

이와 같이 system 보안과 관련된 명령들을 **privilege operation**이라고 하며, <span style="background:#fff88f">mode bit가 0일때만 수행</span>할 수 있다.

> 모든 I/O operation은 privilege operation이다

User program이 disk에 저장된 file을 자유롭게 볼수 있다면 보안상 문제가 발생할 수 있다. 가령, 내꺼가 아닌 file에 접근해서 트롤링하면 큰일난다.. 그래서 <span style="background:#fff88f">모든 I/O operation은 privilege operation으로 규정</span>하고, user program이 마음대로 I/O 관련 명령을 수행할수 없다. 따라서, I/O가 필요할때는 <span style="background:#fff88f">system call을 통해 OS에 요청</span>해야 한다. 당연히 I/O는 특권명령이기 때문에 mode bit = 0 일때만 할 수 있다.

## Memory 보안

Disk뿐만 아니라 <span style="background:#fff88f">memory에도 보안이 필요</span>하다. Multiple programs들이 memory에 **동시에** 올라가서 실행되기 때문에, <span style="background:#fff88f">하나의 user program이 다른 프로그램이나 OS에 위치한 memory space를 침범할 수 있기때문</span>이다. 적어도 <span style="background:#fff88f">interrupt vector</span>와 <span style="background:#fff88f">interrupt service routine</span>이 있는 곳은 각별한 보안이 필요하다. 왜냐하면 user program이 interrupt service routine을 조져놔서 이상한 코드로 바꿔버리면 큰일나기 때문이다.

이를 위해, **base register**과 **limit register** 2개의 레지스터를 사용한다. <span style="background:#fff88f">Base registor은 프로그램이 합법적으로 접근할수있는 memory상의 가장 작은 주소를 보관</span>하고 있고, <span style="background:#fff88f">limit register은 base register로부터 접근 할 수 있는 메모리의 범위</span>를 보관하고 있다.

즉, 어떤 프로그램이 memory address를 할때마다 "<span style="background:#fff88f">하드웨어"적으로 현재 접근하려는 위치가 "합법적"인 위치에 있는지 확인</span>한다. <span style="background:#fff88f">(base, base + limit)</span>. 만약 불법적 메모리 접근이면 **exception**이 발생하고 OS에게 **software interrupt**를 발생시키고, OS는 CPU control을 해당 프로그램으로부터 빼앗고 강제로 종료시킨다.

[NOTE] 위에 설명한 단순한 base, limit register은 <span style="background:#fff88f">단순화된 메모리 관리 기법을 사용하는 경우 한정</span>이다. 실제로는 **paging** 기법을 사용하며, 이 경우에는 더 복잡한 지원이 필요하다.

- <span style="background:#fff88f">Memory address operation은 특권 명령이 아니다</span>! 다만, user program이 메모리에 접근하기전에 하드웨어적으로 합법적인지 체크하며 메모리를 보호하는것이다. 다만,<span style="background:#fff88f"> base & limit register을 바꾸는건 당연히 privilege operation</span>이다.

## 11. CPU 보호

하나의 컴퓨터에 하나의 CPU만 존재한다고 가정할때, <span style="background:#fff88f">특정 프로그램이 infinite loop등으로 CPU를 독점하면 큰일난다</span>. 따라서 **timer**라는 <span style="background:#fff88f">hardware device</span>를 사용해 <span style="background:#fff88f">CPU가 하나의 프로그램으로부터 독점되는 것을 막는다</span>.

Timer은 <span style="background:#fff88f">정해진 시간이 지나면, interrupt을 발생시켜 OS가 CPU control를 뺴앗아 다른 program에게 CPU을 이양</span>하는 것이다. 타이머는 일정한 시간단위로 감소하며 매 <span style="background:#fff88f">click tick</span>마다 <span style="background:#fff88f">1씩 감소</span>하고, <span style="background:#fff88f">0이 되면 interrupt</span>를 발생한다. 여기서, timer 값을 세팅하는 명령을 **load timer**이라고 하며, 이는 <span style="background:#fff88f">privilege operation</span>에 속한다. 한편, 타이머는 time-sharing system에서 <span style="background:#fff88f">현재 시간을 계산하기 위해서도 사용</span>하기도 한다.

## 12. System call을 이용한 I/O 수행

위에서도 말했듯이, <span style="background:#fff88f">disk에 file write</span>, <span style="background:#fff88f">file read</span>, <span style="background:#fff88f">keyboard로 입력을 받거나</span>, <span style="background:#fff88f">모니터에 출력</span>하는 행위들은 모두 I/O에 해당되므로, 전부 **privilege operation**이다. 따라서,<span style="background:#fff88f"> user program이 직접 수행할수가 없으므로</span> **system call**이라는걸 통해 OS에 대행 요청을 한다.

System call은 일종의 **software interrupt**로서, 이걸 할 경우 **trap**이 발생해, CPU control을 OS로 넘기게 된다. 그러면 OS가 입출력 연산을 하고, (ex. disk I/O였다면)disk controller가 다끝내면 CPU에게 interrupt를 쏴서 I/O가 끝났다고 알려주면, CPU control을 다시 user program에 넘기게 된다.

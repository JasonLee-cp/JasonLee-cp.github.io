---
layout: post
title: "Ch5 - Process Management"
subtitle: "운영체제와 정보기술의 원리 책을 공부하고 기록한 포스팅 입니다."
categories: dev
tags: os
comments:
---

"운영체제와 정보기술의 원리" 책 5장을 공부하고 기록한 글 입니다.

## Process 개념

**Process**란 실행 중인 프로그램 (<span style="background:#fff88f">program in exeuction</span>)을 뜻한다. Disk에서 executable file형태로 존재하던 프로그램이 memory에 올라가서 execute이 되면 비로소 생명력을 갖는 process가 된다. 일반적으로 **job**이라는 용어로도 부르기도 한다.

> **Process Context**

<span style="background:#fff88f">Process</span>를 <span style="background:#fff88f">이해하기 위해서는</span> 프로세스의 문맥(**context**)에 대해 잘 이해해야 하는데.. context란 process가 현재 어떤 상태에서 실행되고 있는지 정확하기 규명하기 위해서 필요한 정보를 의미한다.

Time-sharing system에서는 process가 실행되고 CPU를 뺏기고 다시 획득하고...왔다갔다 하는데, 이떄 CPU를 다시 획득해 수행을 재개할때 "<span style="background:#fff88f">이전의 CPU 보유 시기에 어느 부분까지 명령을 수행했는지, 직전 수행 시점의 정확한 상태"를 재현</span>해야 한다. 이때, 정확한 재현을 위해 필요한 정보가 바로 context이다.

즉, process context는 그 프로세스의 **address space**(code, data, stack), **register value**, system call 등을 통해 **kernel에서 수행한 일의 상태**, **process에 관해 kernel이 관리하는 각종 정보** 등을 포함하게 된다.

Process의 문맥을 크게 3가지로 분류하면

1. **Hardware context**
   - <span style="background:#fff88f">CPU의 수행상태</span>를 나타내는것
   - <span style="background:#fff88f">PC</span>, <span style="background:#fff88f">각종 register value</span>
2. **Address space**
   - process는 code, data, stack으로 구성되는 자신만의 <span style="background:#fff88f">address space</span>를 갖고있다.
3. **Kernel context**
   - <span style="background:#fff88f">OS는 process를 관리하기 위한 data structure을 유지</span>한다
   - <span style="background:#fff88f">PCB</span>와 <span style="background:#fff88f">kernel stack</span>

## 2. Process status

![](/assets/img/os/os5_1.png)
Process는 매시점 어떠한 status에 놓여지게 된다. 대표적으로는

1. **New** (시작)
   - <span style="background:#fff88f">process가 시작되어 각종 data structure은 생성</span>되었지만, <span style="background:#fff88f">아직 memory 획득을 승인받지 못한 상태</span>
2. **Ready** (준비)
   - <span style="background:#fff88f">CPU 만 보유하면 당장 instruction을 실행</span>할수 있지만, CPU를 <span style="background:#fff88f">할당받지 못한 상태</span>
3. **Running** (실행)
   - <span style="background:#fff88f">process가 CPU를 보유하고, machine instruction을 실행</span>하고 있는 상태
4. **Blocked, wait, sleep** (봉쇄)
   - <span style="background:#fff88f">CPU를 할당받더라도 당장 명령을 실행할 수 없는 상태</span>
   - ex) 프로세스가 요청한 I/O 작업이 진행중인 경우
5. **Terminated** (완료)
   - process가 종료되었으나 OS가 그 process와 관련된 <span style="background:#fff88f">data structure을 완전히 정리하지 못한 상태</span>

> **Context switch**

하나의 process는 어느 한 상태에 머물게 되는데, 시간에 따라 바뀐다.

예를들어, running state에서 timer interrupt가 발생하면, CPU control은 OS도 이양된다. 그러면 OS는 timer interrupt service routine으로 가서 수행 중이던 process context를 저장하고 ready state로 바꾸고, ready state에 있는 프로세스를 적절하게 선택하고 running state가 된다. 이처럼 원래 process context를 저장하고 새로운 process의 context를 세팅하는 과정을 **context switch**.

Context switch가 일어나는 경우는 <span style="background:#fff88f">timer interrupt</span> 외에도 <span style="background:#fff88f">I/O request</span> 등으로 blocked state로 바뀌는 경우가 있다. 이때, <span style="background:#fff88f">ready state에 있는 process가 CPU control을 넘겨받는</span> <span style="background:#fff88f">과정</span>을 **dispatch** 라고 한다.

> **Process 상태 변화 예시**

1. Process A: Running state에 있는 <span style="background:#fff88f">process A가 disk file read 작업을 요청</span>한다
2. <span style="background:#fff88f">A는 blocked state</span>로 바뀌고 CPU가 ready state의 process들 중에서 하나 <span style="background:#fff88f">B를 선정해 CPU를 할당</span>하고, <span style="background:#fff88f">B는 running state</span>가 된다.
3. 이때, <span style="background:#fff88f">A는 disk I/O를 기다리는 queue에 서있다가</span> 자기 차례가 되어 disk controller로 부터 데이터를 받고나면, disk <span style="background:#fff88f">controller가 CPU에게 interrupt</span>를 발생시켜 I/O 완료 신호를 보낸다
4. 그러면 CPU는 B를 실행하고 있다가, interrupt를 확인하고 그에 대응하는 루틴을 수행한다. 이 루틴이 진행되는 동안 <span style="background:#fff88f">B의 상태</span>는 <span style="background:#fff88f">user mode running state</span>에서 <span style="background:#fff88f">kernel mode running state</span>로 바뀐다. 비록 interrupt service routine이 B랑은 무관한걸 하고있지만, 인터럽트 처리를 위해 <span style="background:#fff88f">"편의상" 직전 process context에서 실행된 것으로 간주</span>한다. 다시 말해, <span style="background:#fff88f">process가 실행되던 중에 interrupt가 발생하면, interrupt가 발생한 원인과 관계없이 interrupt를 당한 process (B)가 user mode에서 실행되다가 kernel mode로 진입한 것으로 간주</span>하게 된다
5. Disk controller가 발생시킨 <span style="background:#fff88f">interrupt</span>는 I/O 작업이 완료된 process <span style="background:#fff88f">A의 상태를 blocked에서 ready로 바꾼</span>후 장치의 <span style="background:#fff88f">local buffer에 있는 내용을 memory로 이동</span>시키는 일련의 업무를 수행한다.
6. 이렇게 interrupt 처리가 끝나면, <span style="background:#fff88f">interrupt service routine 이전에 수행되던 process에게 CPU를 다시 할당</span>해, 그 process 직전 수행 시점 이후의 코드가 실행된다. 경우에 따라서는 interrupt를 당한 process에게 CPU를 다시 할당안하고, I/O 마친 프로세스에게 할당하기도 하는데, 이건 스케쥴러가 결정한다.

---

## 3. PCB (Process Control Block)

PCB란 OS가 <span style="background:#fff88f">시스템내의 process들을 관리하기 위해 process 마다 유지하는 정보들을 담는 </span>
<span style="background:#fff88f">kernel내의 data structure</span>을 말한다. PCB는 다음과 같은 요소들고 구성된다,

![](/assets/img/os/os5_2.png)

1. **process state**
   - <span style="background:#fff88f">CPU를 할당해도 되는지 여부를 결정</span>하기 위해 필요하다
2. **PC value**
   - 다음에 수행할 <span style="background:#fff88f">instruction address</span>
3. **CPU register value**
   - CPU 연산을 위해 현 시점에 register에 저장하고 있는 값
4. **CPU scheduling information**
   - process의 <span style="background:#fff88f">CPU scheduling</span>을 위해 필요한 정보
5. **memory management information**
   - process의 <span style="background:#fff88f">메모리 할당</span>을 위해 필요한 정보
6. **accounting information** (자원 사용 정보)
   - user에게 <span style="background:#fff88f">resource usage </span>요금을 계산해 청구하는 등의 용도로 사용된다
7. **I/O status information**
   - process가 오픈한 file 정보 등 process의 <span style="background:#fff88f">I/O 관련 상태 정보</span>를 나타낸다

## 4. Context switch

**Context switch**란 "<span style="background:#fff88f">하나의 user process로부터 다른 user process로 CPU control이 transfer되는 과정</span>"을 뜻한다.
![](/assets/img/os/os5_3.png)

예를들어, Process A가 CPU를 할당받고 실행되던 중에 <span style="background:#fff88f">timer interrupt</span>가 발생하면,

1. CPU control을 A에서 CPU로 넘기게 된다.
2. OS는 timer interrupt service routine으로 가서 A의 context를 저장하고 새로운 process B에게 CPU를 이양한다
   - 이 과정에서 A는 ready state가 되고 B는 running state가 된다
   - context switch중에 <span style="background:#fff88f">A는 context를 자신의</span> **PCB**에 저장하고, B는 예전에 저장했던 context를 <span style="background:#fff88f">PCB로부터 실제 hardware로 복원 </span>시킨다

Context switch는 <span style="background:#fff88f">timer interrupt외에도</span> A가 I/O request나 다른 조건을 충족하지 못해 CPU를 회수당하고 <span style="background:#fff88f">blocked state</span>가 되는 경우에도 발생할수 있다.

[NOTE] Process A가 running일때 syscall이나 interrupt가 발생하면, CPU control이 OS로 넘어와, A를 멈추고 kernel code가 실행된다. 이 경우에도 CPU의 실행 위치 등 process context중 일부를 PCB에 저장하게 되지만, 이러한 과정을 **context switch라 하지는 않는다**. 이는 **running mode**가 user mode에서 kernel모드로 바뀌는것일 뿐이다.
![](/assets/img/os/os5_4.png)

> **Context switch is a heavy overhead**

Context switch가 일어나는 동안에는 실제 system에게 useful한 작업이 일어나지 않기때문에 overhead이며, 매우 빨라야한다.

## 5. Process Scheduling Queue

![](/assets/img/os/os5_5.png)
![](/assets/img/os/os5_6.png)

> **Queue - Hardware resources**

OS는 <span style="background:#fff88f">ready state에 있는 process들을 줄세우기 위해</span> **ready queue**를 두고, ready queue의 젤 앞에 있는 애한테 CPU를 먼저 할당한다. 큐에 줄세우는 방법은 <span style="background:#fff88f">scheduling</span> 방법에 따라 달라진다.

Ready queue외에도 OS는 특정 resource를 기다리는 process들을 줄세우기 위해 device별로 **device queue**를 둔다. 예를들어, disk에 I/O service를 요청한 process들은 **disk I/O queue**에 줄 서게 된다. 그러면 disk controller는 disk I/O queue에 줄서있는 순서대로 process의 I/O 작업을 수행한다. 프로세스별 작업이 완료되면 disk controller가 CPU에 interrupt를 발생시키고, 그러면 interrupt service routine에 의해, 완료된 process은 device queue를 빠져나와 ready queue에 줄서게 된다. 이 외에도, **keyboard I/O queue** 등등 장치마다 있다.

> **Queue - software resources**

![](/assets/img/os/os5_7.png)

Queue는 <span style="background:#fff88f">소프트웨어 자원</span>을 기다리는 경우에도 필요하다. 예를들어, **shared data**에 대한 <span style="background:#fff88f">접근 권한은 software resource로 분류</span>될 수 있는데, 어떠한 process가 shared data를 사용하는 중에, 다른 process가 이걸 접근하면 <span style="background:#fff88f">data consistency</span>가 훼손될 수 있기 때문에, shared data는 <span style="background:#fff88f">"매 시점 하나의 process"</span>만이 접근할수 있게 해야한다.

이때, <span style="background:#fff88f">"접근</span>" 한다는것이 <span style="background:#fff88f">반드시 CPU가 그 데이터를 사용하고 있음을 의미하는건 아니다</span>. Shared data에 접근 중인 process가 <span style="background:#fff88f">ready state나 blocked state로 변경</span><span style="background:#fff88f">된 경우에도</span>, 새롭게 CPU를 할당받은 프로세스가 동일한 데이터에 접근하게 되면 consistency issue가 발생할수있으므로 쉽게 접근을 허락해서는 안된다.

즉, shared data라는 일종의 software resource를 앞서 <span style="background:#fff88f">접근 중인 process가 다 사용하고 "반납"할때까지는 다른 proceess가 CPU를 할당받았다 하더라도, 접근하</span><span style="background:#fff88f">지 말고 기다려야 한다</span>. 따라서, 여러 process가 shared data에 동시 접근하려고 할 경우, shared data를 기다리는 queue에 줄서게하여 현재 그 데이터를 사용하고 있는 <span style="background:#fff88f">process가 data를 반납하기 전까지는 접근하지 못하게하고</span>, 반납하면 큐 순서대로 접근권한을 주는 방법을 사용하게 된다.

이와 같이 process state 관리는 **kernel address space** 중 **data area**에 <span style="background:#fff88f">다양한 queue를 두어 수행</span>하게 된다. 각 process가 CPU를 기다리는지, I/O를 기다리는지 등의 정보를 <span style="background:#fff88f">kernel이 총체적으로 관리</span>한다.

예를들어, <span style="background:#fff88f">timer interrupt</span>가 발생하면 <span style="background:#fff88f">kernel은 자신의 data area에 있는 ready queue를 참조</span>해, 다음 어느 process에게 CPU를 줄지 결정하고, 현재 실행중인 애는 큐에 맨 뒤로 보낸다.

> **Job queue**

OS는 ready queue와 device queue외에도 **job queue** (작업 큐)를 유지한다. Job queue는 <span style="background:#fff88f">"시스템 내의 모든 process를 관리하기 위한 queue"</span>로서, <span style="background:#fff88f">process state과 무관하게 현재 시스템 내의 모든 프로세스가 job queue에 속하게 된다</span>. 그러므로 job queue에 있다고해서 <span style="background:#fff88f">반드시 memory를 가지고 있는건 아니다</span>. Job queue가 가장 넓은 개념이고 ready queue와 device queue에있는 애들은 모두 job queue에 속해있다.

각 queue는 **queue header**를 유지하며, <span style="background:#fff88f">큐는 각 process의 PCB를 linked list 형태로 관리</span>하며, <span style="background:#fff88f">pointer를 사용해 순서를 정한다</span>. Process가 CPU를 할당받고 코드를 수행하다가 I/O request가 발생하면 device queue에 가서 줄서게 된다. Device queue에 속한 process들은 blocked state에 있다가 끝나면 device controller가 interrupt를 발생시키고, 다시 ready state로 바껴서 ready queue로 이동한다.

## 6. Scheduler

**Scheduler**이란, "<span style="background:#fff88f">어떤 process에게 resource를 할당할지를 결정하는 OS kernel code"</span>를 뜻한다. 스케쥴러는 크게 **long term scheduler**, **medium term scheduler**, 그리고 **short term scheduler**이 있다.

1. **Long-term scheduler** (Job scheduler)
   - 어떤 process를 ready queue에 넣을지 결정하는 역할을 한다
   - Ready queue는 CPU만 얻으면 당장 실행될수있는 process들의 집합이고, CPU에서 실행되기 위해서는 memory에 올라가 있어야 하니까, 즉, <span style="background:#fff88f">"process에게 memory를 할당하는 역할"</span>을 한다
   - 처음 process가 생성되어 new state에 있는데, 이떄 long term scheduler은 <span style="background:#fff88f">new process들 중 어떤 process를 ready queue에 삽입할지 결정하는 역할</span>을 한다
   - <span style="background:#fff88f">Degree of multiprogramming</span> (memory에 동시에 올라가있는 process들의 수)를 조절하는 역할을 한다
   - 현대의 time-sharing system에서는 <span style="background:#fff88f">일반적으로 long-term scheduler를 두지않는다</span>. 과거에는 resource가 매우 빈약해 썼는데 <span style="background:#fff88f">요즘은 process가 시작 상태가 되면 long-term scheduler없이 바로 memory에 할당해 ready queue에 넣어주게 된다</span>.
2. **Medium-term scheduler**
   - 현대의 time-sharing system에서는 long-term scheduler대신 <span style="background:#fff88f">medium-term scheduling</span>을 쓴다
   - 너무 많은 Process에게 memory를 할당해 시스템 성능이 저하되는 경우, 이를 해결하기 위해 <span style="background:#fff88f">"memory에 적재된 process 수를 dynamically 조절"</span>하기 위해 추가된 스케쥴러
   - 많약 너무 많은 process들이 memory에 올라가서 process마다 보유하고 있는 memory가 극도로 적어지면, CPU가 당장 필요한 process의 address space조차도 메모리에 올려놓기 어려운 상황이 발생한다. 그러면 disk I/O가 수시로 발생돼 속도가 심각하게 저하될수 있다.
   - 이런 경우, <span style="background:#fff88f">"memory에 올라가있는 process들 중 일부를 선정해 이들로부터 memory를 통째로 빼앗아 disk의 swap area에 저장"</span>한다 (swap out)
   - Swap out의 <span style="background:#fff88f">0순위는 "blocked state"</span>에 있는 process들이다. 그래도 부족하면 보통 <span style="background:#fff88f">timer interrupt가 발생해 ready queue로 이동하는 process</span>를 추가적으로 swap out시킨다.
   - Long-term scheduler와 마찬가지고 <span style="background:#fff88f">degree of multiprogramming</span>을 조절한다
3. **Short-term scheduler** (CPU scheduler)
   - <span style="background:#fff88f">Ready state의 process들 중에서 어떤 process를 다음번에 running 상태</span>로 만들것인지 결정한다
   - time-sharing system에서는 <span style="background:#fff88f">timer interrupt가 발생하면 short-term scheduler</span>이 호출된다.

> **Scheduler마다 고유한 특성을 가진다**

1. **Long-term scheduler**
   - <span style="background:#fff88f">수십 초 내지 수 분 단위</span>로 가끔 호출되기 때문에 <span style="background:#fff88f">좀 느려도 된다</span>
2. **Short-term scheduler**
   - <span style="background:#fff88f">milisecond 단위로 매우 빈번</span>하게 호출되기 때문에 <span style="background:#fff88f">속도가 빨라야 한다</span>

> **Suspended state**

Medium-term scheduler의 등장으로 **suspended state**가 더 추가된다. Suspended state는 <span style="background:#fff88f">"external reason"으로 process 수행이 중지된 상태</span>를 뜻한다. Suspended state에 있는 process들은, <span style="background:#fff88f">"외부에서 재개시키지 않는이상 다시 활성화될수 없으므로 memory resource가 당장 필요하지 않다"</span>. 따라서, suspended state의 process는 <span style="background:#fff88f">memory를 통째로 빼앗기고 disk로 swap out</span>된다.

Medium-term scheduler에 의해 disk에 swap out된 process가 대표적인 suspended state의 예라고 할 수 있다.

Suspended state는 **suspended-ready**와 **suspended-blocked** state로 나눌 수 있다.

**Suspended ready**:<span style="background:#fff88f"> Ready state</span>에 있던 Process가 medium-term scheduler에 의해 <span style="background:#fff88f">swap out되는 경우</span>
**Suspended blocked**: <span style="background:#fff88f">Blocked state</span>에 있던 process가 medium-term scheduler에 의해 <span style="background:#fff88f">swap out되는 경우</span>

<span style="background:#fff88f">Suspended blocked state</span>이던 프로세스가 blocked되었던 condition을 만족하게 되면, <span style="background:#fff88f">suspended ready state</span>로 바뀐다.

Suspended state에 있는 process들은 위의 두 경우 모두 <span style="background:#fff88f">memory를 조금도 보유하지 않고, disk에 통째로 swap-out된 상태로 존재</span>하게 된다.

## 7. Process Creation

![](/assets/img/os/os5_8.png)
시스템이 부팅된 후 <span style="background:#fff88f">최초의 process는 OS가 직접 생성</span>하지만, <span style="background:#fff88f">그 다음부터는 parent process가 child process를 복제 생성</span>한다. 이런 방식을 통해 hierarchy를 생성한다. 프로세스의 세계에서는 <span style="background:#fff88f">자식이 먼저 죽고, 죽은 자식의 처리는 부모가 담당</span>하는 방식으로 진행된다. 만약 후손을 많이 생성한 경우는 단계적으로 그 프로세스가 생성했던 <span style="background:#fff88f">모든 chidlren을 연쇄적으로 종료시킨 후에야 본인이 종료</span>될 수 있다.

생성된 process가 작업을 수행하기 위해서는 <span style="background:#fff88f">resource</span>가 필요하다. Resource를 획득하는 방식도 OS 및 resource 종류에 따라 다른데, 어떤 경우에는 <span style="background:#fff88f">OS로 부터 직접 자원을 할당</span>받을수도 있고, 또 다른 경우는 <span style="background:#fff88f">parent process와 resource를 공유</span>해서 사용할 수도 있다.

Process가 수행되는 모델도

1. <span style="background:rgba(3, 135, 102, 0.2)">Parent process와 child process가 공존하며 수행되는 모델</span>
   - 둘이 <span style="background:#fff88f">CPU 놓고 경쟁</span>
2. <span style="background:rgba(3, 135, 102, 0.2)">Parent가 child의 종료를 기다리는 모델</span> -
   _ <span style="background:#fff88f">Child process가 종료될때까지</span> <span style="background:#fff88f">parent는 아무 일도 하지 않고 blocked state</span>에 머물러 있다가, 자식이 종료되면 그때 parent는 ready state이 되어 CPU 권한을 얻는다.
   _ 예를들어, shell이 있다
   ![](/assets/img/os/os5_9.png)

> **Child process의 address space**

Process가 생성되면 자신만의 <span style="background:#fff88f">독자적인 address space</span>를 갖게 된다. Parent process가 child를 생성하면, child는 <span style="background:#fff88f">parent와는 "별도의 address space"</span>를 가지게 되는데, 처음 address space를 생성할 때는 <span style="background:#fff88f">parent의 address space를 "그대로 복사"</span>해서 생성하고, child가 <span style="background:#fff88f">다른 프로그램을 수행하기 위해서는</span> 생성된 address space위에 새로운 프로그램의 address space를 <span style="background:#fff88f">"덮어씌워 실행"</span>하게 된다. (**copy-on-write**)

> **UNIX에서의 process creation**

![](/assets/img/os/os5_10.png)

UNIX에서는 `fork()` 라는 <span style="background:#fff88f">s</span><span style="background:#fff88f">ystem call</span>을 통해 parent의 내용을, **PID를 제외하고** <span style="background:#fff88f">그대로 "복제 생성"</span>하게 된다. 따라서, <span style="background:#fff88f">child process는 비록 address space를 따로 갖게 되지만</span>, 그 <span style="background:#fff88f">address space내에는 동일한 내용</span>을 가지게 된다. fork()를 통해 생성된 child process는 `exec()` system call을 통해, <span style="background:#fff88f">새로운 프로그램으로 address space를 덮어씌울수있다</span>.

> **Process의 종료**

원칙적으로 parent process가 종료되기 전에 그 아래에 존재하는 모든 children이 먼저 종료되어야 한다. 이와 관련해 process termination은 두가지로 나뉜다

1. "**자발적 종료**": Process가 마지막 instruction을 수행한후 OS에게 이를 알려 이루어진다
   - process는 instruction을 모두 수행한 후, 끝에 `exit()`라는 syscall을 넣어주도록 되어있다. 즉, <span style="background:#fff88f">process는 system call을 통해 OS에게 자신이 종료됨을 알린</span>다. 그러면 OS는 이 프로세스로부터 resource를 회수하고, 시스탬내에서 이 프로세스를 정리하게 된다.
   - 한편, `exit()` 함수는 개발자가 명시적으로 호출하지 않아도 프로그램이 종료되는 지점에 compiler가 <span style="background:#fff88f">자동으로 삽입</span>해 process의 종료 직전에 항상 호출된다
2. **비자발적 종료**: Parent process가 child process의 수행을 `abort()`라는 함수를 통해 강제로 종료시킨다
   - [<span style="background:#fff88f">CASE 1</span>] Child process가 할당 resource의 한계를 넘어서는 많은 양의 resource를 요구할때
   - [<span style="background:#fff88f">CASE 2</span>] Child process에게 할당된 작업이 더 이상 필요하지 않을 때
   - [<span style="background:#fff88f">CASE 3</span>] Parent process가 종료(exit) 될 때
     - 이 경우에는, parent이 종료되면 child는 더이상 수행되지 못하기 때문에 단계적인 종료가 발생한다

> **로그아웃 후에도 계속 프로세스를 실행시키고 싶을 떄**

User account로 서버에 접속해서 수행시킨 프로그램을, <span style="background:#fff88f">logout후에도 계속 수행시켜야 하는 경우</span>가 있을 수 있는데, 이 경우 logout을 하게되면, login창 아래에 생성된 모든 child process들이 종료되기 때문에, 계속 실행시키고 싶으면, 해당 <span style="background:#fff88f">process를 로그아웃 후에도 계속 존재하는 system process로 이양시키는 절차</span>가 필요하다.

즉, 종료되는 process의 child를 계속 실행시키기 위해선, 종료되지 않을 다른 process의 "양자"로 보내는 것이다. 이러면 부모가 죽기전에 자식이 먼저 죽게 된다는 원칙이 여전히 지켜지는 것이다.

> **How parent creates child?**

OS는 child process의 생성을 위해 `fork()` system call을 제공한다. Process가 `fork()` system call을 하게 되면 CPU control이 kernel로 넘어가게 되고, kernel은 `fork()`를 호출한 process를 복제해, child process를 생성하게 된다.

즉, `fork()` syscall을 하게되면, `fork()`를 호출한 프로세스와 <span style="background:#fff88f">"똑같은 process"</span>가 생성된다. 실제로 child process는 parent process와 **모든 context를 동일하게 가지고 있다**. 즉, parent process의 address space를 비롯해 <span style="background:#fff88f">PC</span>, <span style="background:#fff88f">register value</span>, <span style="background:#fff88f">PCB</span>, <span style="background:#fff88f">kernel stack</span>등 <span style="background:#fff88f">PID를 제외하고 모든 context를 그대로 복제</span>해 child process의 context를 형성하게 된다. 따라서, child process는 parent의 처음부터 수행하는게 아니라, <span style="background:#fff88f">호출한 시점부터 (PC 지점)실행</span>하게 된다는 것이다.

한가지 <span style="background:#fff88f">child process를 구분</span> 할 수 있는건

1. `return fork() = positive`: **parent**
2. `return fork() = 0`: **child**

> **exec()**

이처럼 `fork()` syscall을 통해 process를 생성한후 그 return value에 따라 parent과 child에게 서로다른 작업을 수행시킬 수는 있지만, 이건 그냥 branching일 뿐, 사실당 두 process는 모두 동일한 코드의 내용을 가질 수밖에 없다. <span style="background:#fff88f">따라서, child에게 부모와는 다른 독자적인 프로그램을 수행시킬 수 있는 메커니즘</span>이 필요하다. UNIX에서는 process의 address space에 새로운 프로그램을 덮어씌우는 `exec()` syscall을 지원한다.

`exec()` syscall은 프로세스가 <span style="background:#fff88f">지금까지 수행했던 상태를 모두 잊어버리고, 그 address space를 완전히 새로운 프로그램으로 덮어씌운 후, 새로운 프로그램의 첫 부분부터 다시 실행</span>을 시작하도록하는 syscall이다. 따라서, 새로운 프로그램을 실행시키기 위해서는 `fork()`로 복제한후, `exec()`을 통해 새롭게 수행시키려는 프로세스를 child의 address space에 덮어씌우면 된다.

> `fork()`와 `exec()`은 privilege operation이다

Process creation과 관련된 두 함수는 user process가 직접할수없는 **privilege operation**이다. 따라서, system call을 통해서만 수행할 수 있다.

> **wait()**

`fork()`, `exec()`, `exit()` 외에도 `wait()`이라는 함수가 있는데, `wait()` syscall은 child process가 종료되기를 기다리며 parent process가 <span style="background:#fff88f">blocked state</span>에 머무르도록 할 때 사용된다. `fork()`후에 `wait()`을 호출하면, <span style="background:#fff88f">kernel은 child process가 종료될때까지 parent process를 blocked state에 머무르게 하</span>고, <span style="background:#fff88f">child process가 종료되면 parent를 ready state로 변경시켜 작업을 재개</span>할 수 있도록 한다. 이러한 방식으로 부모와 자식간에 **synchronization**이 가능해진다.

`wait()` 을 한 후, parent는 일반적인 blocked state에서처럼 resource를 기다리는 것이 아니라, child process가 종료되기를 기다리며 수면상태에 머무르게 되는 것이며, child가 종료되면 다시 **ready queue**에 넣어져 CPU를 얻을 권한을 획득한다.

## 8. IPC (Inter Process Communication)

<span style="background:#fff88f">Process는 각자 자신만의 독립적인 address space</span>를 가지고 있으므로, <span style="background:#fff88f">process A가 다른 process B의 address space에 접근하는것은 "원칙적"으로는 허용되지 않는다</span>. 하지만, <span style="background:#fff88f">경우에 따라서는, process들이 협력할때 업무의 효율성이 좋아질수가 있다</span>. 부분적인 처리 결과나 정보를 공유할수있는 등 효율적인 측면이 있다. 따라서, OS는 **IPC (Inter-Process Commmunication)** 을 제공한다.

> **IPC 란?**

IPC란 <span style="background:#fff88f">"하나의 컴퓨터 안에서 실행 중인 서로 다른 process간에 발생하는 communication"</span>을 말한다. 이러한 메커니즘에서는 <span style="background:#fff88f">communication뿐만 아니라</span>,<span style="background:#fff88f"> 공유 데이터를 보호</span>하기 위한 **syncrhonization** 메커니즘도 있어야 한다. 즉, IPC가 하는 일은 크게 **(1) communication** 과 **(2) synchronization**으로 볼수 있다.

> **IPC의 2가지 방법: message passing & shared memory**

IPC의 대표적인 방법으로는 **message passing**과 **shared memory**가 있다. 이 두 방식의 차이는 <span style="background:#fff88f">process사이에 shared data를 사용하는가, 그렇지 않는가</span>에 있다.

> **1. Message Passing**

Message passing 방식은, <span style="background:#fff88f">process간에 shared data를 일체 사용하지 않고, 메시지를 주고받으면서 통신하는 방</span>식을 뜻한다. 이때, 두 process의 address space가 다르므로, message를 직접 전달 할 수 는 없고, **kernel**을 통해 소통을 하게된다.

Message passing을 하는 시스템은 <span style="background:#fff88f">kernel</span>에 의해 `send(message)` `receive(message)`라는 두 연산을 제공받는데, 이 연산들을 통해 process는 전달할 메세지를 OS에게 **system call**방식으로 요청해 전달할 수 있다.

Message를 process끼리 직접 전달하면, 원하지 않는 메세지를 전달해 약영향을 끼칠수 있으므로, OS는 message passing operation을 **privilege operation**으로 규정해, kernel을 통해서만 가능하도록 한다.

통신하기를 원하는 두 process는 **communication link**를 생성한 후 `send()`와 `receive()`를 통해, 메세지를 주고받게된다. Communication link의 구현방법은 <span style="background:#fff88f">물리적인 방법</span>과 <span style="background:#fff88f">논리적인 방법</span>이 있다.

Message passing을 통해 전달하는 방식은 <span style="background:#fff88f">message의 전송 대상이 "다른 process"인지 아니면 "mailbox"라는 일종의 저장공간 인지</span>에 따라 다시 **direct communication**인지 **indirect communication**지로 나뉜다. 이 두개의 차이는 연산의 interface에 대한 차이일 뿐, 실제 메세지 전송이 이루어지는 구현은 kernel의 중재에 의해 사실당 동일하게 이루어진다.

1. **Direct Communication**
   - <span style="background:#fff88f">통신하려는 process의 이름을 명시적으로 표시</span>한다
   - `send(P, message)`: P에게 메세지 전송
   - `receive(Q, message)`: Q로부터 메세지를 전달받음
   - 이러한 방식을 위한 communication link는 다음과 같은 특성을 갖는다
     - <span style="background:#fff88f">Link는 자동적으로 생성</span>되고, <span style="background:#fff88f">하나의 link는 정확히 한 쌍의 process에게 할당</span>된다
     - <span style="background:#fff88f">각 쌍의 process에게는 오직 하나의 link만이 존재</span>한다
     - Link는 <span style="background:#fff88f">unidirectional</span>(단방향)일 수는 있으나, <span style="background:#fff88f">대부분 bidirectional</span>(양방향) 이다.
2. **Indirect Communication**
   - Message를 <span style="background:#fff88f">mail box</span> 또는 <span style="background:#fff88f">port</span>로부터 전달받는다
   - 각<span style="background:#fff88f"> mailbox에는 고유한 ID</span>가 있으며, <span style="background:#fff88f">mailbox를 공유하는 process들만 서로 communication</span>을 할 수가 있다.
   - <span style="background:#fff88f">Communication link는 process간에 mailbox를 공유하는 경우에만 생성</span>된다.
   - <span style="background:#fff88f">하나의 link가 여러 process들에게 할당될 수 있으며</span>, <span style="background:#fff88f">각 process의 쌍은 여러 link를 공유할 수 있다</span>.
   - Link는 <span style="background:#fff88f">unidirectional</span>혹은 <span style="background:#fff88f">bidirectional</span>일 수 있다.
   - <span style="background:#fff88f">새로운 mailbox를 생성</span>하는 연산, <span style="background:#fff88f">mailbox를 통한 메세지의 send()/receive()</span> 연산, <span style="background:#fff88f">mailbox를 삭제하는 연산</span> 등이 사용될 수 있다
   - `send(A, mesasage)`: A라는 mailbox에 message를 전송
   - `receive(A, message)`: A라는 milabox로부터 메세지를 전달받는것
   - <span style="background:#ff4d4f">[NOTE]</span> 여러 프로세스들이 mailbox를 공유하기 때문에 다음과 같은 문제점이 발생할수있다. 만약 `P1, P2, P3`가 `mailbox A`를 공유하는 경우, `P1`이 메세지를 보냈다면, `P2, P3`중 <span style="background:#fff88f">어느 프로세스가 메세지를 받게 되는가?</span> 이러한 의문을 해결하기 위해...
     - [Solution 1] <span style="background:#fff88f">2개의 process에게만 link를 할당</span>하는 방법이 사용될 수 있다. 즉 P2와 P3에게 각각 따로 link를 생성하는 것이다.
     - [Solution 2] Link에 대한 `receive()` 연산을 <span style="background:#fff88f">매 시점 하나의 process만 수행</span>할 수 있도록 하는 방법이 있다.
     - [Solution 3] <span style="background:#fff88f">시</span><span style="background:#fff88f">스템이 message receiver을 임의로 결정</span>해, 누가 message를 받았는지 sender에게 통신해주는 방식이 있다.

> **2. Shared memory**

IPC의 또 다른 방식으로는 **shared memory** 방식이 있다. Shared memory방식에서는 <span style="background:#fff88f">process들이 address space의 일부분을 공유</span>한다.

원칙적으로 서로 다른 프로세스는 각자 독립적인 address space가 있지만, <span style="background:#fff88f">OS가 shared memory를 사용하는 system call을 지원해, 서로 다른 process들이 그들의 address space중 일부를 공유</span>할 수 있도록 한다.

이러한 <span style="background:#fff88f">shared memory 영역은 각자의 address space에 공통적으로 포함되는 영역이</span>므로, 여러 <span style="background:#fff88f">process가 읽고 쓰는것이 가능</span>하다.

실제 implementation은 process A와 B가 서로 독자적인 address space를 가지고 있지만, 이 address space이 <span style="background:#fff88f">physical memory에 mapping될 때, shared memory area에 대해서는 동일한 memory address로 매핑</span>되는 것이다.

Shared memory방식은 process간의 통신을 수월하게 만든는 interface를 제공하지만, 서로의 <span style="background:#fff88f">data에 consistency</span> 문제가 발생될 수 있다. 이에 대해서는 kernel이 책임지지 않기 때문에, 프로세스들끼리 <span style="background:#fff88f">직접 syncrhonization을 맞춰야 한다</span>.

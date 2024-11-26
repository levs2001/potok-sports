ref: лекция 6
Нужно сделать оконную обработку, видимо по ключу
```
stream
.keyBy(...)
.window(...) // Определяем назначитель окна.
.reduce/aggregate/process(...) // Определяем оконную функцию.

// Определяем оконный оператор без ключа.
stream
.windowAll(...) // Определяем назначитель окна.
.reduce/aggregate/process(...) // Определяем оконную функцию.
```

Скользящее окно:
```
// Назначитель скользящего окна времени события.
val slidingAvgTemp = sensorData
.keyBy(_.id)
// Создаем окно времени событий длиной 1 час каждые 15 минут.
.window(SlidingEventTimeWindows.of(Time.hours(1), Time.minutes(15)))
.process(new TemperatureAverager)

// Назначитель скользящего окна времени обработки.
val slidingAvgTemp = sensorData
.keyBy(_.id)
// Создаем окно времени обработки длиной 1 час каждые 15 минут.
.window(SlidingProcessingTimeWindows.of(Time.hours(1), Time.minutes(15)))
.process(new TemperatureAverager)

```

Дока по флинку:
https://nightlies.apache.org/flink/flink-docs-master/docs/try-flink/local_installation/

Лучше использовать java api.

Есть Application Mode (там прям в образ нашу джобу надо подсунуть) 
и Session Mode (как я понял, он может разные джобы на вход принимать)

Судя по доке лучше использовать session mode, он используется в getting started
https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/resource-providers/standalone/docker/#starting-a-session-cluster-on-docker

Скорее всего, в first step именно session mode https://nightlies.apache.org/flink/flink-docs-master/docs/try-flink/local_installation/

Разворачивать через докер или скриптом с сайта, надо подумать.

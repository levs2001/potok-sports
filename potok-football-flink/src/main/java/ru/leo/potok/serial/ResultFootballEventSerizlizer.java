package ru.leo.potok.serial;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import javax.annotation.Nullable;
import lombok.AllArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.apache.flink.connector.kafka.sink.KafkaRecordSerializationSchema;
import org.apache.kafka.clients.producer.ProducerRecord;
import ru.leo.potok.domain.ResultFootballEvent;

@Log4j2
@AllArgsConstructor
public class ResultFootballEventSerizlizer implements KafkaRecordSerializationSchema<ResultFootballEvent> {
    private static final ObjectMapper objectMapper = new ObjectMapper();

    private final String topic;

    @Nullable
    @Override
    public ProducerRecord<byte[], byte[]> serialize(ResultFootballEvent element, KafkaSinkContext context, Long timestamp) {
        var key = String.format("%s_%s_%d", element.getLeague(), element.getResultScore(), timestamp).getBytes();
        byte[] value;
        try {
            value = objectMapper.writeValueAsBytes(element);
        } catch (JsonProcessingException e) {
            log.error("Can't deserialize result football event", e);
            throw new IllegalArgumentException("Can't deserialize result football event", e);
        }
        return new ProducerRecord<>(topic, key, value);
    }
}

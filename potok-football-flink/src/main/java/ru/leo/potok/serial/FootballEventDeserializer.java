package ru.leo.potok.serial;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;
import lombok.extern.log4j.Log4j2;
import org.apache.flink.api.common.serialization.AbstractDeserializationSchema;
import org.apache.flink.api.common.serialization.DeserializationSchema;
import ru.leo.potok.domain.FootballEvent;

@Log4j2
public class FootballEventDeserializer extends AbstractDeserializationSchema<FootballEvent> {
    private static final ObjectMapper objectMapper = new ObjectMapper();

    @Override
    public FootballEvent deserialize(byte[] message) throws IOException {
        try {
            var res = objectMapper.readValue(message, FootballEvent.class);
            log.info("Remapped value: {}", res);
            return res;
        } catch (IOException e) {
            log.error("Error during football event deserialization.", e);
            throw e;
        }
    }

    public static void main(String[] args) {
        DeserializationSchema<FootballEvent> s = new FootballEventDeserializer();
    }
}

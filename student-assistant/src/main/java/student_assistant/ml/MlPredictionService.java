package student_assistant.ml;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

import java.util.Map;

@Service
public class MlPredictionService {

    private final RestClient restClient;

    public MlPredictionService() {
        this.restClient = RestClient.builder()
                .baseUrl("http://localhost:5000")
                .build();
    }

    public Map predictScore(Map studentData) {
        return restClient.post()
                .uri("/predict")
                .body(studentData)
                .retrieve()
                .body(Map.class);
    }
}
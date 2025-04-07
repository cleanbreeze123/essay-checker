import { useState } from "react";
import { Textarea } from "@/components/ui/textarea";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

export default function EssayFeedbackApp() {
  const [prompt, setPrompt] = useState("학생에게 제시할 논술형 문항을 입력하세요.");
  const [studentAnswer, setStudentAnswer] = useState("");
  const [feedback, setFeedback] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    setLoading(true);
    // Simulated AI feedback process
    setTimeout(() => {
      setFeedback(
        "✅ 주제에 부합함\n✅ 논리적 흐름 양호\n⚠️ 결론이 약함 - 핵심 주장의 반복이나 요약 필요\n⚠️ 일부 문장이 모호함 - 예시 추가 권장"
      );
      setLoading(false);
    }, 1500);
  };

  return (
    <div className="grid gap-4 max-w-3xl mx-auto p-6">
      <motion.h1 className="text-2xl font-bold text-center" initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
        AI 논술 피드백 도우미
      </motion.h1>

      <Card>
        <CardContent className="grid gap-2 p-4">
          <label className="font-medium">📝 논술형 문항</label>
          <Textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} rows={3} />
        </CardContent>
      </Card>

      <Card>
        <CardContent className="grid gap-2 p-4">
          <label className="font-medium">👩‍🎓 학생 답안</label>
          <Textarea
            placeholder="여기에 학생 답안을 입력하거나 붙여넣으세요."
            value={studentAnswer}
            onChange={(e) => setStudentAnswer(e.target.value)}
            rows={6}
          />
        </CardContent>
      </Card>

      <Button onClick={handleAnalyze} disabled={loading} className="w-full">
        {loading ? "분석 중..." : "AI 피드백 생성하기"}
      </Button>

      {feedback && (
        <motion.div
          className="bg-green-100 p-4 rounded-xl text-sm whitespace-pre-line border border-green-400"
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <strong>📊 AI 피드백 결과:</strong>
          <div className="mt-2">{feedback}</div>
        </motion.div>
      )}
    </div>
  );
}


import opennlp.tools.chunker.ChunkerME;
import opennlp.tools.chunker.ChunkerModel;
import opennlp.tools.cmdline.PerformanceMonitor;
import opennlp.tools.cmdline.postag.POSModelLoader;
import opennlp.tools.namefind.NameFinderME;
import opennlp.tools.namefind.TokenNameFinderModel;
import opennlp.tools.postag.POSModel;
import opennlp.tools.postag.POSSample;
import opennlp.tools.postag.POSTaggerME;
import opennlp.tools.tokenize.Tokenizer;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;
import opennlp.tools.tokenize.WhitespaceTokenizer;
import opennlp.tools.util.ObjectStream;
import opennlp.tools.util.PlainTextByLineStream;
import opennlp.tools.util.Span;

import java.io.*;
import java.lang.reflect.Array;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;


public class NERChunker {

    public static void main(String[] args) throws IOException {

        chunkFile("/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/raw/reuters.raw", "opennlp_reuters.chunk");
        chunkFile("/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/Aritter/raw/arriter_tweet_chunk_corpora.txt", "opennlp_aritter.chunk");
//        chunkFile("/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/CoNLL-2000/raw/wsj2000.raw", "opennlp_wsj2000.chunk");

        findEntities("/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Conll/raw/reuters.raw","opennlp_reuters.ner");
        findEntities("/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/Twitter/Aritter/raw/arriter_tweet_ner_corpora.txt","opennlp_aritter.ner");
        findEntities("/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/dados/MSM2013/tweets.txt","opennlp_msm2013.ner");
    }

    public static void chunkFile(String inputFilename,String outputFilename) throws IOException {
//        POSModel posModel = new POSModelLoader()
//                .load(new File("/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/Experiments/Tools/apache-opennlp-1.6.0/models/en-pos-maxent.bin"));
        POSModel posModel = new POSModelLoader()
                .load(new File("/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/Experiments/Tools/apache-opennlp-1.6.0/models/en-pos-perceptron.bin"));
        POSTaggerME posTagger = new POSTaggerME(posModel);

        List<String> list = Files.readAllLines(Paths.get(inputFilename), StandardCharsets.UTF_8);
        String[] lines = list.toArray(new String[list.size()]);


        float counter=0,nLines=lines.length;
        PrintWriter pw = new PrintWriter(new FileWriter(outputFilename));
        for (String line:lines){
            ObjectStream<String> lineStream = new PlainTextByLineStream(
                    new StringReader(line));

            InputStream tokenizerModel = new FileInputStream("/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/Experiments/Tools/apache-opennlp-1.6.0/models/en-token.bin");
            TokenizerModel token_model = null;

            try {
                token_model = new TokenizerModel(tokenizerModel);
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            finally {
                if (tokenizerModel != null) {
                    try {
                        tokenizerModel.close();
                    }
                    catch (IOException e) {
                    }
                }
            }
            Tokenizer learnableTokenizer;
            learnableTokenizer = new TokenizerME(token_model);
            String tokens[] = null;
            String[] posTags = null;
            while ((line = lineStream.read()) != null) {
                tokens = learnableTokenizer.tokenize(line);
                posTags = posTagger.tag(tokens);
            }

            String[] chunks=performIOBChunking(tokens,posTags);

            for(int i=0;i<chunks.length;i++) {
                pw.write(tokens[i] + " " + chunks[i] + "\n");
            }
            pw.write(" \n");
            counter++;
            System.out.println("Progress: " + counter + " / " + nLines + "("+counter/nLines*100+" % )"+"\n");
        }
        pw.close();




    }

    public static String[] performIOBChunking(String[] tokens,String[] posTags) throws IOException {

        String chunkerModel="/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/Experiments/Tools/apache-opennlp-1.6.0/models/en-chunker.bin";
        InputStream is = new FileInputStream(chunkerModel);
        ChunkerModel cModel = new ChunkerModel(is);

        ChunkerME chunkerME = new ChunkerME(cModel);
        String chunks[] = chunkerME.chunk(tokens, posTags);

        return chunks;
    }

    public static void findEntities(String inputFilename,String outputFilename) throws IOException {
        String [] models={"/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/Experiments/Tools/apache-opennlp-1.6.0/models/en-ner-person.bin",
        "/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/Experiments/Tools/apache-opennlp-1.6.0/models/en-ner-location.bin",
        "/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/Experiments/Tools/apache-opennlp-1.6.0/models/en-ner-organization.bin"};

        List<String> list = Files.readAllLines(Paths.get(inputFilename), StandardCharsets.UTF_8);
        String[] lines = list.toArray(new String[list.size()]);

        float counter=0,nLines=lines.length;
        PrintWriter pw = new PrintWriter(new FileWriter(outputFilename));
        for (String line:lines) {
            ObjectStream<String> lineStream = new PlainTextByLineStream(
                    new StringReader(line));

            InputStream tokenizerModel = new FileInputStream("/home/alexpnt/DEI/MEI/NEW_MEI/REMINDS-Internship/Experiments/Tools/apache-opennlp-1.6.0/models/en-token.bin");
            TokenizerModel token_model = null;

            try {
                token_model = new TokenizerModel(tokenizerModel);
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                if (tokenizerModel != null) {
                    try {
                        tokenizerModel.close();
                    } catch (IOException e) {
                    }
                }
            }
            Tokenizer learnableTokenizer;
            learnableTokenizer = new TokenizerME(token_model);
            String tokens[] = null;
            String[] posTags = null;
            while ((line = lineStream.read()) != null) {
                tokens = learnableTokenizer.tokenize(line);
            }



            int m=0;
            String[] tags = new String[tokens.length];
            Arrays.fill(tags,"O");
            for(String model:models) {
                InputStream fModel = new FileInputStream(model);
                TokenNameFinderModel entityModel = new TokenNameFinderModel(fModel);
                fModel.close();

                NameFinderME nameFinder = new NameFinderME(entityModel);


                Span nameSpans[] = nameFinder.find(tokens);
                for (Span s : nameSpans){
                    for (int i = s.getStart(); i < s.getEnd() ; i++) {
                        if(m==0)
                            tags[i]="PER";
                        else if (m==1)
                            tags[i]="LOC";
                        else
                            tags[i]="ORG";
                    }
                }
                m++;
            }


            for (int i = 0; i < tokens.length; i++) {
//                System.out.println(tokens[i]+" "+tags[i]);
                pw.write(tokens[i]+" "+tags[i]+"\n");
            }
            pw.write("\n");
            counter++;
            System.out.println("Progress: " + counter + " / " + nLines + "("+counter/nLines*100+" % )"+"\n");
        }
        pw.close();
    }
}

import { Module } from '@nestjs/common';
import { AppGateway } from './app.gateway';
import { DetectionServiceGateway } from './detection-service.gateway';

@Module({
  imports: [],
  controllers: [],
  providers: [AppGateway, DetectionServiceGateway],
})
export class AppModule {}

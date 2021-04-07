export class LabelDto {
  name: string;
  color: string;
  fg: string;
}

export class BBoxDto {
  rect: number[];
  label: LabelDto;
}

export class DetectionDto {
  image: string;
  boxes: BBoxDto[];
}
